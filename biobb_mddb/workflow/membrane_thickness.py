#!/usr/bin/env python3

"""Module containing the MembraneThickness class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis


class MembraneThickness(MddbAnalysis):
    """
    | biobb_mddb MembraneThickness
    | Wrapper of the `Membrane thickness analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/thickness.py>`_ module.
    | Calculate the membrane thickness as the distance between leaflet phosphate planes along the trajectory, using a sampling of frames. The system must include a membrane. Lipids are identified automatically, but non-standard lipid residue names may be forced through the forced_lipids field in the inputs file.

    Args:
        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_topology.tpr>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_inputs.json>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).
        output_analysis_filepath (str): Membrane thickness analysis results. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_membrane_thickness.json>`_. Accepted formats: json (edam:format_3464).
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

            from biobb_mddb.workflow.membrane_thickness import membrane_thickness

            prop = {}
            membrane_thickness(input_topology_filepath='/path/to/topology.prmtop',
                               input_structure_filepath='/path/to/structure.cif',
                               input_trajectory_filepath='/path/to/trajectory.xtc',
                               output_analysis_filepath='/path/to/membrane_thickness.json',
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
    flag = 'thickness'
    outputs = {
        'output_analysis_filepath': ('file', 'mda.thickness.json'),
    }

    def __init__(self, input_topology_filepath: str,
                 input_structure_filepath: str,
                 input_trajectory_filepath: str,
                 output_analysis_filepath: str,
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
                'output_analysis_filepath': output_analysis_filepath,
            }
        }


        # Check the properties
        self.check_properties(properties)
        # Check the arguments
        self.check_arguments()


def membrane_thickness(input_topology_filepath: str,
                       input_structure_filepath: str,
                       input_trajectory_filepath: str,
                       output_analysis_filepath: str,
                       input_inputs_filepath: str | None = None,
                       properties: dict | None = None, **kwargs) -> int:
    """Create :class:`MembraneThickness <workflow.membrane_thickness.MembraneThickness>` class and
    execute the :meth:`launch() <workflow.membrane_thickness.MembraneThickness.launch>` method."""
    return MembraneThickness(**dict(locals())).launch()


membrane_thickness.__doc__ = MembraneThickness.__doc__
main = MembraneThickness.get_main(membrane_thickness, 'Membrane thickness along the trajectory.')


if __name__ == '__main__':
    main()
