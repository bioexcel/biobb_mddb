#!/usr/bin/env python3

"""Module containing the Clusters class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis
from biobb_common.generic.biobb_object import launcher


class Clusters(MddbAnalysis):
    """
    | biobb_mddb Clusters
    | Wrapper of the `Clusters analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/clusters.py>`_ module.
    | Cluster the frames of the trajectory according to the conformation of every interaction and find the transitions between clusters. A screenshot is generated for every cluster. Interactions must be defined, either through the interactions property or the inputs file.

    Args:
        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).
        output_analysis_zip_path (str): Zip file with the analysis summary (mda.clusters.json), one results file per interaction and the cluster screenshots. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **pbc_selection** (*str*) - (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
            * **cg_selection** (*str*) - (None) Atom selection (VMD syntax) of Coarse Grained beads. Use 'auto' to guess them. If not set, the value in the inputs file is used, or none by default.
            * **interactions** (*list*) - (None) List of interactions to be analyzed. Each interaction is a dictionary with the fields name, agent_1, selection_1, agent_2, selection_2 and optionally distance_cutoff (Å). Selections are in VMD syntax. If not set, interactions in the inputs file are used.
            * **md_type** (*str*) - (None) Type of molecular dynamics. If not set, the value in the inputs file is used, or 'trajectory' by default. Values: trajectory (Frames are consecutive in time), ensemble (Frames are not related in time).
            * **framestep** (*float*) - (None) Time between consecutive frames in nanoseconds (ns). If not set, the value in the inputs file is used.
            * **binary_path** (*str*) - ("mwf") Path to the MDDB workflow executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Path to the binary executable of your container.
            * **container_image** (*str*) - ("ghcr.io/mmb-irb/mddb_wf:latest") Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash -c") Path to the binary executable of the container shell.

    Examples:
        This is a use example of how to use the building block from Python::

            from biobb_mddb.workflow.clusters import clusters

            prop = {
                'interactions': [{
                    'name': 'protein-ligand interaction',
                    'agent_1': 'protein', 'selection_1': 'protein',
                    'agent_2': 'ligand', 'selection_2': 'resname LIG'
                }]
            }
            clusters(input_topology_filepath='/path/to/topology.prmtop',
                     input_structure_filepath='/path/to/structure.cif',
                     input_trajectory_filepath='/path/to/trajectory.xtc',
                     output_analysis_zip_path='/path/to/clusters.zip',
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
    flag = 'clusters'
    outputs = {
        'output_analysis_zip_path': ('zip', None),
    }
    input_fields = {'pbc_selection': 'pbc_selection', 'cg_selection': 'cg_selection', 'interactions': 'interactions', 'md_type': 'type', 'framestep': 'framestep'}
    input_defaults = {'type': 'trajectory'}

    def __init__(self, input_topology_filepath: str,
                 input_structure_filepath: str,
                 input_trajectory_filepath: str,
                 output_analysis_zip_path: str,
                 input_inputs_filepath: str | None = None,
                 properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())


clusters = launcher(Clusters)


if __name__ == '__main__':
    Clusters.main()
