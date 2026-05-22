#!/usr/bin/env python3

"""Module containing the RmsdPerResidue class and the command line interface."""
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger
from pathlib import PurePath
import shutil


class RmsdPerResidue(BiobbObject):
    """
    | biobb_mddb RmsdPerResidue
    | Wrapper of the `RMSD per residue analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/rmsd_per_residue.py>`_ module.
    | Calculate average and standard deviation RMSD per residue for every residue in a system using a sampling of frames along the trajectory.

    Args:
        input_topology_filepath (str): Input topology or structure file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/topology.top>`_. Accepted formats: pdb (edam:format_1476), gro (edam:format_2033), prmtop (edam:format_3881), top (edam:format_3880), itp (edam:format_3883), tpr (edam:format_2333), psf (edam:format_3882).
        input_trajectory_filepath (str): Input trajectory file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/trajectory.dcd>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), dcd (edam:format_3878), nc (edam:format_3650).
        output_analysis_filepath (str): Analysis results file. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/mda.rmsd_perres.json>`_. Accepted formats: json (edam:format_3464).
        properties (dic):
            * **skip_processing** (*bool*) - (False) Do not process input files, assuming they were already processed.
            * **binary_path** (*str*) - ("mwf") Example of executable binary property.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None)  Path to the binary executable of your container.
            * **container_image** (*str*) - ("mddb/mddb:latest") Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mddb.workflow.workflow import rmsd_per_residue

            prop = { 'skip_processing': False }
            rmsd_per_residue(input_topology_filepath='/path/to/my_topology.prmtop',
                    input_trajectory_filepath='/path/to/my_trajectory.dcd',
                    output_analysis_filepath='/path/to/results.json',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: MDDB Workflow
            * version: >=0.1.10
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    def __init__(self, input_topology_filepath: str, input_trajectory_filepath: str,
                 output_analysis_filepath: str, properties=None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Modify to match constructor parameters
        # Input/Output files
        self.io_dict = {
            'in': {
                'input_topology_filepath': input_topology_filepath,
                'input_trajectory_filepath': input_trajectory_filepath,
            },
            'out': {
                'output_analysis_filepath': output_analysis_filepath,
            }
        }

        # Properties specific for BB
        self.skip_processing = properties.get('skip_processing', False)
        self.binary_path = properties.get('binary_path', 'mwf')
        self.properties = properties

        # Check the properties
        self.check_properties(properties)
        # Check the arguments
        self.check_arguments()

    @launchlogger
    def launch(self) -> int:
        """Execute the :class:`RmsdPerResidue <workflow.rmsd_per_residue.RmsdPerResidue>` object."""

        # Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Parse filepaths
        input_topology_filepath = self.stage_io_dict['in']['input_topology_filepath']
        input_trajectory_filepath = self.stage_io_dict['in']['input_trajectory_filepath']

        # Container paths
        sandbox = self.stage_io_dict.get("unique_dir", "")
        if self.container_path:
            sandbox = self.container_volume_path

        # Prepare the command line parameters as instructions list
        instructions = []
        if self.skip_processing:
            instructions.append('--faith')
            fu.log('Appending optional boolean property', self.out_log, self.global_log)

        # Build the actual command line as a list of items (elements order will be maintained)
        replica_subdirectory = 'replica_1'
        expected_output_filepath = replica_subdirectory + '/perres/mda.rmsd_perres.json'
        self.cmd = [(f'{self.binary_path} run -dir {sandbox} -i perres -top {input_topology_filepath} '
                     f'-md {replica_subdirectory} {input_trajectory_filepath}'), *instructions]
        if self.container_path:
	    self.cmd.append('; chmod a+w -R' + str(PurePath(sandbox).joinpath(replica_subdirectory)))
        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        # Run Biobb block
        self.run_biobb()

        # Move output file to the expected location
        expected_output_filepath_abs = str(PurePath(self.stage_io_dict['unique_dir']).joinpath(expected_output_filepath))
        fu.log(f"copy {expected_output_filepath_abs} {self.io_dict['out']['output_analysis_filepath']}", self.out_log, self.global_log)
        shutil.copy(expected_output_filepath_abs, self.io_dict['out']['output_analysis_filepath'])

        # Copy files to host
        self.copy_to_host()

        # Remove temporary file(s)
        self.tmp_files.extend([replica_subdirectory, "topology.prmtop"]) 
        self.remove_tmp_files()

        # Check output arguments
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def rmsd_per_residue(input_trajectory_filepath: str, input_topology_filepath: str = None,
                     output_analysis_filepath: str = None, properties: dict | None = None,
                     **kwargs) -> int:
    """Create :class:`Workflow <workflow.rmsd_per_residue.RmsdPerResidue>` class and
    execute the :meth:`launch() <workflow.rmsd_per_residue.RmsdPerResidue.launch>` method."""
    return RmsdPerResidue(**dict(locals())).launch()


rmsd_per_residue.__doc__ = RmsdPerResidue.__doc__
main = RmsdPerResidue.get_main(rmsd_per_residue, 'RMSD per residue using the MDDB workflow.')


if __name__ == '__main__':
    main()

# 12. Complete documentation strings
