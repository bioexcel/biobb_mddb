#!/usr/bin/env python3

"""Common base class for the MDDB workflow building blocks: the input processing and the analyses."""
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from pathlib import Path, PurePath
from glob import glob
import shlex
import shutil
import json
import yaml
import os

# Name of the MD directory where the workflow writes all MD outputs
REPLICA_DIRECTORY = 'replica_1'
# Name of the inputs file written by the building block in the sandbox
BIOBB_INPUTS_FILENAME = 'biobb_mddb_inputs.json'
# Prefix used to rename staged input files, so they never collide with workflow output filenames
# e.g. an input named 'topology.prmtop' would be overwritten by the workflow output topology
STAGED_INPUT_PREFIX = 'biobb_mddb_'


class MddbAnalysis(BiobbObject):
    """
    | biobb_mddb MddbAnalysis
    | Base class for MDDB workflow analyses and input processing. Not a building block by itself.

    Subclasses must set the following class attributes:
        * **flag**: The workflow task flag (e.g. 'perres'), as in the '-i' argument of 'mwf run'.
        * **outputs**: Dictionary where keys are output arguments and values are tuples of (output type, workflow output filename).
          Output types are 'file' (a single file in the outputs directory, filename may be a glob pattern matching one file),
          'zip' (the whole outputs directory zipped) and 'glob' (a set of files in the outputs directory, zipped). Filename is a glob pattern in the latter.
          The outputs directory is the analysis directory of the replica, see _outputs_directory().
        * **processed_inputs**: True (default) if the inputs are already processed (e.g. the outputs of the input processing block),
          so the workflow skips the processing and checking steps ('--faith').
        * **input_fields**: Dictionary where keys are property names and values are inputs file field names.
          Properties which are not None are written to the inputs file passed to the workflow.
        * **input_defaults**: Dictionary with default values for inputs file fields, used when the field is set neither by properties nor by the user inputs file.
        * **cli_properties**: Dictionary where keys are property names and values are workflow command line flags.
          Properties which are not None are passed to the workflow through the command line.
          Boolean properties are flags: passed alone when True and not passed when False.
        * **cli_inputs**: Dictionary where keys are additional input file arguments and values are workflow command line flags.

    Args:
        properties (dic):
            * **binary_path** (*str*) - ("mwf") Path to the MDDB workflow executable binary.
    Examples:
        Not a building block.
    """
    flag: str = ''
    outputs: dict = {}
    processed_inputs: bool = True
    input_fields: dict = {}
    input_defaults: dict = {}
    cli_properties: dict = {}
    cli_inputs: dict = {}

    def _stage_input(self, key: str) -> str | None:
        """Stage an input file under a safe name in the sandbox and return its path for the command line.
        Note that the workflow may write outputs with the same name than the input file.
        """
        original_filepath = self.io_dict['in'].get(key)
        if not original_filepath: return None
        unique_dir = self.stage_io_dict['unique_dir']
        filename = Path(original_filepath).name
        safe_filename = f'{STAGED_INPUT_PREFIX}{key}{Path(filename).suffix}'
        safe_host_filepath = Path(unique_dir).joinpath(safe_filename)
        if safe_host_filepath.is_symlink() or safe_host_filepath.exists(): safe_host_filepath.unlink()
        # If the sandbox is disabled then input files are not copied, so we link the original file
        # Otherwise we rename the copy in the sandbox
        # Note that a link to the copy is not enough, since the workflow resolves links before checking names
        if self.disable_sandbox:
            safe_host_filepath.symlink_to(Path(original_filepath).resolve())
            self.tmp_files.append(str(safe_host_filepath))
        else:
            Path(unique_dir).joinpath(filename).rename(safe_host_filepath)
        return str(PurePath(self.sandbox).joinpath(safe_filename))

    def _write_inputs_file(self) -> str | None:
        """Write the workflow inputs file in the sandbox and return its path for the command line.
        The user inputs file (if any) is used as base and then input properties are added.
        If there are no inputs at all then no file is written, since the workflow does not accept empty inputs files.
        """
        inputs = {}
        user_inputs_filepath = self.io_dict['in'].get('input_inputs_filepath')
        if user_inputs_filepath:
            with open(user_inputs_filepath) as file:
                if Path(user_inputs_filepath).suffix == '.json': inputs = json.load(file)
                else: inputs = yaml.safe_load(file) or {}
        for property_name, field in self.input_fields.items():
            value = getattr(self, property_name)
            if value is None: continue
            inputs[field] = value
        for field, value in self.input_defaults.items():
            if inputs.get(field) is None: inputs[field] = value
        if len(inputs) == 0: return None
        host_filepath = Path(self.stage_io_dict['unique_dir']).joinpath(BIOBB_INPUTS_FILENAME)
        with open(host_filepath, 'w') as file:
            json.dump(inputs, file, indent=4)
        self.tmp_files.append(str(host_filepath))
        return str(PurePath(self.sandbox).joinpath(BIOBB_INPUTS_FILENAME))

    def _get_extra_arguments(self) -> list[str]:
        """Additional command line arguments for the workflow."""
        arguments = []
        for property_name, flag in self.cli_properties.items():
            value = getattr(self, property_name)
            if value is None or value is False: continue
            arguments += [flag] if value is True else [flag, value]
        for input_key, flag in self.cli_inputs.items():
            staged_filepath = self._stage_input(input_key)
            if staged_filepath is None: continue
            arguments += [flag, staged_filepath]
        return arguments

    def _outputs_directory(self) -> Path:
        """Go from the sandbox to the directory of the workflow outputs: the analysis directory of the replica."""
        return Path(self.stage_io_dict['unique_dir'], REPLICA_DIRECTORY, self.flag)

    def _collect_outputs(self):
        """Copy workflow outputs from the outputs directory to the sandbox output paths."""
        outputs_directory = self._outputs_directory()
        if not outputs_directory.exists():
            raise FileNotFoundError(f'The workflow did not generate the outputs directory {outputs_directory}')
        for output_key, (output_type, workflow_filename) in self.outputs.items():
            sandbox_output_filepath = self.sandbox_file(output_key)
            # Optional outputs which were not requested
            if not sandbox_output_filepath: continue
            if output_type == 'file':
                workflow_filepaths = glob(str(outputs_directory.joinpath(workflow_filename)))
                if len(workflow_filepaths) == 0:
                    raise FileNotFoundError(f'The workflow did not generate the expected output file {workflow_filename}. '
                        f'Check the workflow logs. Outputs directory content: {os.listdir(outputs_directory)}')
                if len(workflow_filepaths) > 1:
                    raise RuntimeError(f'There are multiple files which could be the output {output_key}: {", ".join(workflow_filepaths)}')
                fu.log(f'Copy {workflow_filepaths[0]} --> {sandbox_output_filepath}', self.out_log, self.global_log)
                shutil.copy(workflow_filepaths[0], sandbox_output_filepath)
            elif output_type in ('zip', 'glob'):
                pattern = '*' if output_type == 'zip' else workflow_filename
                workflow_filepaths = sorted(glob(str(outputs_directory.joinpath(pattern))))
                if len(workflow_filepaths) == 0:
                    raise FileNotFoundError(f'The workflow did not generate any output file matching {pattern} in {outputs_directory}. '
                        'Check the workflow logs.')
                fu.log(f'Zip {len(workflow_filepaths)} files --> {sandbox_output_filepath}', self.out_log, self.global_log)
                fu.zip_list(sandbox_output_filepath, workflow_filepaths, self.out_log)
            else: raise ValueError(f'Unknown output type {output_type}')

    def run(self) -> None:
        """Execute the MDDB workflow task of the block."""

        # The path to the sandbox as seen by the workflow: it runs in the sandbox (the container volume in containers)
        self.sandbox = '.'

        # Stage input files with safe names
        input_topology_filepath = self._stage_input('input_topology_filepath')
        input_structure_filepath = self._stage_input('input_structure_filepath')
        input_trajectory_filepath = self._stage_input('input_trajectory_filepath')
        inputs_filepath = self._write_inputs_file()

        # Build the command line
        # The input processing has no input structure (it writes the processed one)
        # Use the 'faith' argument to skip the processing and checking steps of inputs which are already processed
        self.cmd = [self.binary_path, 'run',
                    '-dir', self.sandbox,
                    '-i', self.flag,
                    '-top', input_topology_filepath,
                    *(['-stru', input_structure_filepath] if input_structure_filepath else []),
                    '-md', REPLICA_DIRECTORY, input_trajectory_filepath,
                    *(['--faith'] if self.processed_inputs else []),
                    *self._get_extra_arguments()]
        if inputs_filepath:
            self.cmd += ['-inp', inputs_filepath]
        self.cmd = [shlex.quote(str(item)) for item in self.cmd]
        # Files written inside the container belong to the container user, so make them writable for the sandbox to be removed later
        # Only files owned by the container user are changed (staged inputs are not) and the workflow exit code is kept
        # Note that the container command is wrapped in double quotes, so '$' must be escaped to be expanded inside the container
        if self.container_path:
            self.cmd += ['; status=\\$?;', 'find', self.sandbox, '-user', '\\$(id -u)', '-exec', 'chmod', 'a+w', '{}', '+;', 'exit \\$status']
        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        # Run Biobb block
        unique_dir = self.stage_io_dict['unique_dir']
        previous_entries = set(os.listdir(unique_dir))
        self.run_biobb()
        if self.return_code != 0:
            raise RuntimeError(f'MDDB workflow failed with exit code {self.return_code}. Check the logs.')

        # Without sandbox the workflow writes in the current directory: remove what it added there, not the files that were already there
        # Note that the sandbox is already in the temporary files list unless the sandbox is disabled
        if self.disable_sandbox:
            self.tmp_files.extend(str(Path(unique_dir, entry)) for entry in sorted(set(os.listdir(unique_dir)) - previous_entries))

        # Move output files to the sandbox and then copy them to host
        self._collect_outputs()
