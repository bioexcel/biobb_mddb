#!/usr/bin/env python3

"""Common base class for the MDDB workflow analysis building blocks."""
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
# Workflow files and directories written in the project directory (relative to the sandbox)
WORKFLOW_PROJECT_FILES = ['.mwf_cache.json', '.register.json', 'topology.*', REPLICA_DIRECTORY, 'incomplete_*']


class MddbAnalysis(BiobbObject):
    """
    | biobb_mddb MddbAnalysis
    | Base class for MDDB workflow analyses. Not a building block by itself.

    Subclasses must set the following class attributes:
        * **flag**: The workflow task flag (e.g. 'perres'), as in the '-i' argument of 'mwf run'.
        * **outputs**: Dictionary where keys are output arguments and values are tuples of (output type, workflow output filename).
          Output types are 'file' (a single file in the analysis directory), 'zip' (the whole analysis directory zipped) and
          'glob' (a set of files in the analysis directory, zipped). Filename is a glob pattern in the latter.
        * **input_fields**: Dictionary where keys are property names and values are inputs file field names.
          Properties which are not None are written to the inputs file passed to the workflow.
        * **input_defaults**: Dictionary with default values for inputs file fields, used when the field is set neither by properties nor by the user inputs file.
        * **cli_properties**: Dictionary where keys are property names and values are workflow command line flags.
          Properties which are not None are passed to the workflow through the command line.
        * **cli_inputs**: Dictionary where keys are additional input file arguments and values are workflow command line flags.

    Args:
        properties (dic):
            * **binary_path** (*str*) - ("mwf") Path to the MDDB workflow executable binary.
    Examples:
        Not a building block.
    """
    flag: str = ''
    outputs: dict = {}
    input_fields: dict = {}
    input_defaults: dict = {}
    cli_properties: dict = {}
    cli_inputs: dict = {}

    def __init__(self, properties=None, **kwargs) -> None:
        properties = properties or {}
        # Call parent class constructor
        super().__init__(properties)
        # Properties common to all MDDB workflow analyses
        self.binary_path = properties.get('binary_path', 'mwf')
        self.properties = properties

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
        # Note that in container runs the staged path is the internal container path, so we do not use it
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
            if value is None: continue
            arguments += [flag, value]
        for input_key, flag in self.cli_inputs.items():
            staged_filepath = self._stage_input(input_key)
            if staged_filepath is None: continue
            arguments += [flag, staged_filepath]
        return arguments

    def _collect_outputs(self):
        """Copy workflow outputs from the analysis directory to the sandbox output paths."""
        unique_dir = Path(self.stage_io_dict['unique_dir'])
        analysis_directory = unique_dir.joinpath(REPLICA_DIRECTORY, self.flag)
        if not analysis_directory.exists():
            raise FileNotFoundError(f'The workflow did not generate the analysis directory {analysis_directory}')
        for output_key, (output_type, workflow_filename) in self.outputs.items():
            output_filepath = self.io_dict['out'].get(output_key)
            # Optional outputs which were not requested
            if not output_filepath: continue
            sandbox_output_filepath = str(unique_dir.joinpath(Path(output_filepath).name))
            if output_type == 'file':
                workflow_filepath = analysis_directory.joinpath(workflow_filename)
                if not workflow_filepath.exists():
                    raise FileNotFoundError(f'The workflow did not generate the expected output file {workflow_filepath}. '
                        f'Check the workflow logs. Analysis directory content: {os.listdir(analysis_directory)}')
                fu.log(f'Copy {workflow_filepath} --> {sandbox_output_filepath}', self.out_log, self.global_log)
                shutil.copy(workflow_filepath, sandbox_output_filepath)
            elif output_type in ('zip', 'glob'):
                pattern = '*' if output_type == 'zip' else workflow_filename
                workflow_filepaths = sorted(glob(str(analysis_directory.joinpath(pattern))))
                if len(workflow_filepaths) == 0:
                    raise FileNotFoundError(f'The workflow did not generate any output file matching {pattern} in {analysis_directory}. '
                        'Check the workflow logs.')
                fu.log(f'Zip {len(workflow_filepaths)} files --> {sandbox_output_filepath}', self.out_log, self.global_log)
                fu.zip_list(sandbox_output_filepath, workflow_filepaths, self.out_log)
            else: raise ValueError(f'Unknown output type {output_type}')

    def run(self) -> int:
        """Execute the MDDB workflow analysis."""

        # Set the path to the sandbox as seen by the workflow
        self.sandbox = self.stage_io_dict['unique_dir']
        if self.container_path:
            self.sandbox = self.container_volume_path

        # Stage input files with safe names
        input_topology_filepath = self._stage_input('input_topology_filepath')
        input_structure_filepath = self._stage_input('input_structure_filepath')
        input_trajectory_filepath = self._stage_input('input_trajectory_filepath')
        inputs_filepath = self._write_inputs_file()

        # Build the command line
        # Use the 'faith' argument to always skip the processing and checking steps
        # We asume all MDDB workflow analysis BioBBs are run after a input processing step
        self.cmd = [self.binary_path, 'run',
                    '-dir', self.sandbox,
                    '-i', self.flag,
                    '-top', input_topology_filepath,
                    '-stru', input_structure_filepath,
                    '-md', REPLICA_DIRECTORY, input_trajectory_filepath,
                    '--faith',
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
        self.run_biobb()
        if self.return_code != 0:
            raise RuntimeError(f'MDDB workflow failed with exit code {self.return_code}. Check the logs.')

        # Move output files to the sandbox and then copy them to host
        self._collect_outputs()
        self.copy_to_host()

        # Remove temporary file(s)
        # Note that the sandbox is already in the temporary files list unless the sandbox is disabled
        if self.disable_sandbox:
            for pattern in WORKFLOW_PROJECT_FILES:
                self.tmp_files.extend(glob(str(Path(self.stage_io_dict['unique_dir']).joinpath(pattern))))
        self.remove_tmp_files()

        # Check output arguments
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code
