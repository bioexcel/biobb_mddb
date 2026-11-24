#!/usr/bin/env python3

"""Module containing the HydrogenBonds class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis


class HydrogenBonds(MddbAnalysis):
    """
    | biobb_mddb HydrogenBonds
    | Wrapper of the `Hydrogen bonds analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/hydrogen_bonds.py>`_ module.
    | Find the hydrogen bonds between the agents of every interaction along the trajectory. Interactions must be defined, either through the interactions property or the inputs file.

    Args:
        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).
        output_analysis_zip_path (str): Zip file with the analysis summary (mda.hbonds.json) and one results file per interaction. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **interactions** (*list*) - (None) List of interactions to be analyzed. Each interaction is a dictionary with the fields name, agent_1, selection_1, agent_2, selection_2 and optionally distance_cutoff (Å). Selections are in VMD syntax. If not set, interactions in the inputs file are used.
            * **md_type** (*str*) - (None) Type of molecular dynamics. If not set, the value in the inputs file is used, or 'trajectory' by default. Values: trajectory (Frames are consecutive in time), ensemble (Frames are not related in time).
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

            from biobb_mddb.workflow.hydrogen_bonds import hydrogen_bonds

            prop = {
                'interactions': [{
                    'name': 'protein-ligand interaction',
                    'agent_1': 'protein', 'selection_1': 'protein',
                    'agent_2': 'ligand', 'selection_2': 'resname LIG'
                }]
            }
            hydrogen_bonds(input_topology_filepath='/path/to/topology.prmtop',
                           input_structure_filepath='/path/to/structure.cif',
                           input_trajectory_filepath='/path/to/trajectory.xtc',
                           output_analysis_zip_path='/path/to/hydrogen_bonds.zip',
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
    flag = 'hbonds'
    outputs = {
        'output_analysis_zip_path': ('zip', None),
    }
    input_fields = {'interactions': 'interactions', 'md_type': 'type'}
    input_defaults = {'type': 'trajectory'}

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

        # Properties specific for BB
        self.interactions = properties.get('interactions', None)
        self.md_type = properties.get('md_type', None)


def hydrogen_bonds(input_topology_filepath: str,
                   input_structure_filepath: str,
                   input_trajectory_filepath: str,
                   output_analysis_zip_path: str,
                   input_inputs_filepath: str | None = None,
                   properties: dict | None = None, **kwargs) -> int:
    """Create :class:`HydrogenBonds <workflow.hydrogen_bonds.HydrogenBonds>` class and
    execute the :meth:`launch() <workflow.hydrogen_bonds.HydrogenBonds.launch>` method."""
    return HydrogenBonds(**dict(locals())).launch()


hydrogen_bonds.__doc__ = HydrogenBonds.__doc__
main = HydrogenBonds.get_main(hydrogen_bonds, 'Hydrogen bonds in the interface of every interaction.')


if __name__ == '__main__':
    main()
