#!/usr/bin/env python3

"""Module containing the InputProcessing class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis, REPLICA_DIRECTORY
from biobb_common.generic.biobb_object import launcher
from pathlib import Path

# Alias of the filter property for the default filtering of the workflow (water and counter ions)
DEFAULT_FILTERING_ALIAS = 'def'


class InputProcessing(MddbAnalysis):
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
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash -c") Path to the binary executable of the container shell.

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

    flag = 'inpro'
    # The inputs are raw files: the workflow processes and checks them
    processed_inputs = False
    # The processed topology is in the project directory, with the extension of its format, and the rest in the replica directory
    outputs = {
        'output_topology_filepath': ('file', 'topology.*'),
        'output_trajectory_filepath': ('file', f'{REPLICA_DIRECTORY}/trajectory.xtc'),
        'output_structure_filepath': ('file', f'{REPLICA_DIRECTORY}/structure.cif'),
    }
    cli_properties = {'filter': '-filt', 'image': '-img', 'fit': '-fit'}

    def __init__(self, input_topology_filepath: str, input_trajectory_filepath: str,
            output_topology_filepath: str, output_trajectory_filepath: str,
            output_structure_filepath: str, properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())

    def prepare(self) -> None:
        """Go from the 'def' filter alias to True: the workflow default filtering."""
        if self.filter == DEFAULT_FILTERING_ALIAS: self.filter = True

    def _outputs_directory(self) -> Path:
        """Go from the sandbox to the directory of the processed files: the project directory."""
        return Path(self.stage_io_dict['unique_dir'])


input_processing = launcher(InputProcessing)


if __name__ == '__main__':
    InputProcessing.main()
