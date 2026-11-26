#!/usr/bin/env python3

"""Module containing the InputProcessing class and the command line interface."""
from biobb_common.generic.biobb_object import BiobbObject, launcher
from biobb_common.tools import file_utils as fu
from pathlib import PurePath
from glob import glob
import shutil

# Set some input default values
DEFAULT_OUTPUT_TRAJECTORY_FILENAME = 'trajectory.xtc'
DEFAULT_OUTPUT_STRUCTURE_FILENAME = 'structure.cif'
DEFAULT_FILTERING_ALIAS = 'def'

class InputProcessing(BiobbObject):
    """
    | biobb_mddb InputProcessing
    | Wrapper of the `Input processing steps from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/tools/process_input_files.py>`_ module.
    | Process input raw files by converting, filtering, imaging, fitting, and finally quality-checking the output files.

    Args:
        input_topology_filepath (str): Input topology or structure file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/input_topology.top>`_. Accepted formats: pdb (edam:format_1476), gro (edam:format_2033), prmtop (edam:format_3881), top (edam:format_3880), itp (edam:format_3883), tpr (edam:format_2333), psf (edam:format_3882).
        input_trajectory_filepath (str): Input trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/input_trajectory.dcd>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), dcd (edam:format_3878), nc (edam:format_3650).
        output_topology_filepath (str): Output topology file, with a filtered set of atoms matching the trajectory. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/output_topology.prmtop>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        output_trajectory_filepath (str): Output XTC trajectory file with the filtered, imaged and fitted coordinates. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/output_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        output_structure_filepath (str): Output mmCIF structure file with the filtered, imaged and fitted coordinates. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/output_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        properties (dic):
            * **filter** (*str*) - (False) Removed atoms from the system. A custom atom selection may be passed using VMD selection syntax. Pass the label 'def' to remove water and counter ions by default
            * **image** (*bool*) - (False) Set if the workflow must attempt to automatically image the system (remove Periodic Boundary Conditions where pertinent). WARNING: This is a simple default imaging protocol and may fail in many cases.
            * **fit** (*bool*) - (False) Set if the workflow must attempt to automatically fit the system (remove rotation and translation where pertinent).
            * **binary_path** (*str*) - ("mwf") Path to the MDDB workflow executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None)  Path to the binary executable of your container.
            * **container_image** (*str*) - ("ghcr.io/mmb-irb/mddb_wf:latest") Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mddb.workflow.input_processing import input_processing

            prop = { 'filter': True, 'image': False, 'fit': False }
            input_processing(input_topology_filepath='/path/to/my_topology.prmtop',
                    input_trajectory_filepath='/path/to/my_input_trajectory.dcd',
                    output_topology_filepath='/path/to/output_topology.prmtop',
                    output_trajectory_filepath='/path/to/output_trajectory.xtc',
                    output_structure_filepath='/path/to/output_structure.cif',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: MDDB Workflow
            * version: >=0.1.11
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_topology_filepath: str, input_trajectory_filepath: str,
            output_topology_filepath: str, output_trajectory_filepath: str,
            output_structure_filepath: str, properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())

    def run(self) -> None:
        """Execute the :class:`InputProcessing <workflow.input_processing.InputProcessing>` object."""

        # Parse filepaths
        input_topology_filepath = self.stage_io_dict['in']['input_topology_filepath']
        input_trajectory_filepath = self.stage_io_dict['in']['input_trajectory_filepath']

        # Container paths
        sandbox = self.stage_io_dict.get("unique_dir", "")
        if self.container_path:
            sandbox = self.container_volume_path

        # Prepare the command line parameters as instructions list
        instructions = []
        if self.filter:
            if self.filter == DEFAULT_FILTERING_ALIAS or self.filter is True: instructions.append(f'-filt')
            else: instructions.append(f'-filt "{self.filter}"')
            fu.log('Appending optional boolean property', self.out_log, self.global_log)
        if self.image:
            instructions.append('-img')
            fu.log('Appending optional boolean property', self.out_log, self.global_log)
        if self.fit:
            instructions.append('-fit')
            fu.log('Appending optional boolean property', self.out_log, self.global_log)

        # Build the actual command line as a list of items (elements order will be maintained)
        replica_subdirectory = 'replica_1'
        self.cmd = [(f'{self.binary_path} run -dir {sandbox} -i inpro -top {input_topology_filepath} '
                     f'-md {replica_subdirectory} {input_trajectory_filepath}'), *instructions]
        # DANI: Esto hace falta para los dockers, sino falla al borrar los archivos en /tmp
        # DANI: Otra alternativa es poner el en conf.yml 'remove_tmp: false'
        if self.container_path:
           # Keep the exit code of the workflow, not the one of chmod
           self.cmd.append('; rc=\\$?; chmod a+w -R ' + str(PurePath(sandbox).joinpath(replica_subdirectory)) + '; exit \\$rc')
        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        # Run Biobb block
        self.run_biobb()
        if self.return_code != 0:
            raise RuntimeError(f'MDDB workflow failed with exit code {self.return_code}. Check the logs.')

        # Make sure there is only one possible output topology file
        output_topology_glob = glob(str(PurePath(self.stage_io_dict['unique_dir']).joinpath('topology.*')))
        if len(output_topology_glob) == 0:
            raise FileNotFoundError('The expected output topology file is nowhere to be found')
        if len(output_topology_glob) > 1:
            raise RuntimeError(f'There are multiple files which could be the output topology: {", ".join(output_topology_glob)}')
        expected_output_topology_filename = output_topology_glob[0].split('/')[-1]

        # Copy the output files to their paths in the sandbox, BiobbObject.launch() copies them to the host
        expected_output_filepaths = {
            'output_topology_filepath': expected_output_topology_filename,
            'output_trajectory_filepath': f'{replica_subdirectory}/{DEFAULT_OUTPUT_TRAJECTORY_FILENAME}',
            'output_structure_filepath': f'{replica_subdirectory}/{DEFAULT_OUTPUT_STRUCTURE_FILENAME}',
        }
        for output_key, expected_output_filepath in expected_output_filepaths.items():
            output_filepath = self.sandbox_file(output_key)
            # Optional outputs which were not requested
            if not output_filepath:
                continue
            absolute_filepath = str(PurePath(self.stage_io_dict['unique_dir']).joinpath(expected_output_filepath))
            fu.log(f"copy {absolute_filepath} {output_filepath}", self.out_log, self.global_log)
            shutil.copy(absolute_filepath, output_filepath)

        # Remove temporary file(s)
        if self.disable_sandbox and self.remove_tmp:
            self.tmp_files.extend([replica_subdirectory, expected_output_topology_filename])


input_processing = launcher(InputProcessing)


if __name__ == '__main__':
    InputProcessing.main()

# 12. Complete documentation strings
