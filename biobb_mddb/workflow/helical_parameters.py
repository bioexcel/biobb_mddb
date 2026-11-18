#!/usr/bin/env python3

"""Module containing the HelicalParameters class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis


class HelicalParameters(MddbAnalysis):
    """
    | biobb_mddb HelicalParameters
    | Wrapper of the `Helical parameters analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/helical_parameters.py>`_ module.
    | Calculate the helical parameters, backbone torsions and stiffness of double stranded nucleic acids using Curves+ and Canal. The system must include nucleic acids.

    Args:
        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_topology.prmtop>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).
        output_analysis_zip_path (str): Zip file with all helical parameters analysis results. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **binary_path** (*str*) - ("mwf") Path to the MDDB workflow executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Path to the binary executable of your container.
            * **container_image** (*str*) - ("ghcr.io/mmb-irb/mddb_wf:latest") Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mddb.workflow.helical_parameters import helical_parameters

            prop = {}
            helical_parameters(input_topology_filepath='/path/to/topology.prmtop',
                               input_structure_filepath='/path/to/structure.cif',
                               input_trajectory_filepath='/path/to/trajectory.xtc',
                               output_analysis_zip_path='/path/to/helical_parameters.zip',
                               properties=prop)

    Info:
        * wrapped_software:
            * name: MDDB Workflow
            * version: >=0.1.12
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """
    flag = 'helical'
    outputs = {
        'output_analysis_zip_path': ('zip', None),
    }

    def __init__(self, input_topology_filepath: str,
                 input_structure_filepath: str,
                 input_trajectory_filepath: str,
                 output_analysis_zip_path: str,
                 input_inputs_filepath: str | None = None,
                 properties: dict | None = None, **kwargs) -> None:
        properties = properties or {}

        # Call parent class constructor
        super().__init__(properties)
        self.locals_var_dict = locals().copy()

        # Input/Output files
        self.io_dict = {
            'in': {
                'input_topology_filepath': input_topology_filepath,
                'input_structure_filepath': input_structure_filepath,
                'input_trajectory_filepath': input_trajectory_filepath,
                'input_inputs_filepath': input_inputs_filepath,
            },
            'out': {
                'output_analysis_zip_path': output_analysis_zip_path,
            }
        }


        # Check the properties
        self.check_properties(properties)
        # Check the arguments
        self.check_arguments()


def helical_parameters(input_topology_filepath: str,
                       input_structure_filepath: str,
                       input_trajectory_filepath: str,
                       output_analysis_zip_path: str,
                       input_inputs_filepath: str | None = None,
                       properties: dict | None = None, **kwargs) -> int:
    """Create :class:`HelicalParameters <workflow.helical_parameters.HelicalParameters>` class and
    execute the :meth:`launch() <workflow.helical_parameters.HelicalParameters.launch>` method."""
    return HelicalParameters(**dict(locals())).launch()


helical_parameters.__doc__ = HelicalParameters.__doc__
main = HelicalParameters.get_main(helical_parameters, 'Helical parameters of nucleic acids.')


if __name__ == '__main__':
    main()
