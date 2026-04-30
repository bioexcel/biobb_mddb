#!/usr/bin/env python3

"""Module containing the Template class and the command line interface."""
from pathlib import PurePath
from biobb_common.generic.biobb_object import BiobbObject
from biobb_common.tools import file_utils as fu
from biobb_common.tools.file_utils import launchlogger

from os.path import exists
from shutil import move

class RmsdPerResidue(BiobbObject):
    """
    | biobb_mddb RmsdPerResidue
    | A workflow to process raw MD data into a MDDB-standarized format and run different quality control analyses.

    Args:
        input_topology_filepath (str): Input topology or structure file. File type: input. `Sample file <https://urlto.sample>`_. Accepted formats: pdb (edam:format_1476), gro (edam not found), prmtop (edam:format_3881), top (edam:format_3880) + itp (edam:format_3883), tpr (edam not found), psf (edam:format_3882).
        input_trajectory_filepath (str): Input trajectory file. File type: input. `Sample file <https://urlto.sample>`_. Accepted formats: xtc (edam:format_3875), trr (edam:format_3910), dcd (edam:format_3878), nc (edam:format_3650).
        output_analysis_filepath (str): Analysis results file. File type: output. `Sample file <https://urlto.sample>`_. Accepted formats: json (edam:format_3464).
        properties (dic):
            * **skip_processing** (*bool*) - (False) Do not process input files, assuming they were already processed.
            * **binary_path** (*str*) - ("mwf") Example of executable binary property.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mddb.workflow.workflow import rmsd_per_residue

            prop = { 'boolean_property': False }
            rmsd_per_residue(input_topology_filepath='/path/to/my_topology.prmtop',
                    input_trajectory_filepath='/path/to/my_trajectory.dcd',
                    output_analysis_filepath='/path/to/results.json',
                    properties=prop)

    Info:
        * wrapped_software:
            * name: MDDB Workflow
            * version: >=0.1.10
            * license: Apache License 2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """

    # 2. Adapt input and output file paths as required. Include all files, even optional ones
    def __init__(self, input_topology_filepath : str, input_trajectory_filepath : str,
            output_analysis_filepath : str, properties=None, **kwargs) -> None:
        properties = properties or {}

        # 2.0 Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # 2.1 Modify to match constructor parameters
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

        # 3. Include all relevant properties here as
        # self.property_name = properties.get('property_name', property_default_value)

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

        # 4. Setup Biobb
        if self.check_restart():
            return 0
        self.stage_files()

        # Creating temporary folder
        tmp_folder = self.stage_io_dict.get("unique_dir", "")

        # Parse filepaths
        input_topology_filepath = str(PurePath(tmp_folder).joinpath(PurePath(self.io_dict['in']['input_topology_filepath']).name))
        input_trajectory_filepath = str(PurePath(tmp_folder).joinpath(PurePath(self.io_dict['in']['input_trajectory_filepath']).name))

        # 6. Prepare the command line parameters as instructions list
        instructions = []
        if self.skip_processing:
            instructions.append('--faith')
            fu.log('Appending optional boolean property', self.out_log, self.global_log)

        # 7. Build the actual command line as a list of items (elements order will be maintained)
        replica_subdirectory = 'replica_1'
        self.cmd = [(f'{self.binary_path} run -i perres -top {input_topology_filepath} ' + \
            f'-md {replica_subdirectory} {input_trajectory_filepath}'), *instructions]
        fu.log('Creating command line with instructions and required arguments', self.out_log, self.global_log)

        # 9. Uncomment to check the command line
        print(' '.join(self.cmd))

        # Run Biobb block
        self.run_biobb()

        # Copy files to host
        self.copy_to_host()

        # Make sure the expected output exists internally
        expected_output_filepath = str(PurePath(replica_subdirectory).joinpath(PurePath('perres/mda.rmsd_perres.json')))
        if not exists(expected_output_filepath):
            print(f'Expected output file {expected_output_filepath} is missing')
            return 1
        # Move the output analysis file to the requested output filepath
        output_analysis_filepath = self.io_dict['out']['output_analysis_filepath']
        move(expected_output_filepath, output_analysis_filepath)

        # Remove temporary file(s)
        self.remove_tmp_files()

        # Check output arguments
        self.check_arguments(output_files_created=True, raise_exception=False)

        return self.return_code


def rmsd_per_residue (
    input_trajectory_filepath : str,
    input_topology_filepath : str = None,
    output_analysis_filepath : str = None,
    **kwargs) -> int:
    """Create :class:`Workflow <workflow.rmsd_per_residue.RmsdPerResidue>` class and
    execute the :meth:`launch() <workflow.rmsd_per_residue.RmsdPerResidue.launch>` method."""
    return RmsdPerResidue(**dict(locals())).launch()


rmsd_per_residue.__doc__ = RmsdPerResidue.__doc__
main = RmsdPerResidue.get_main(rmsd_per_residue, 'RMSD per residue using the MDDB workflow.')


if __name__ == '__main__':
    main()

# 12. Complete documentation strings
