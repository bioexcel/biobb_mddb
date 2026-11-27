#!/usr/bin/env python3

"""Module containing the Pockets class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis
from biobb_common.generic.biobb_object import launcher


class Pockets(MddbAnalysis):
    """
    | biobb_mddb Pockets
    | Wrapper of the `Pockets analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/pockets.py>`_ module.
    | Find the most persistent pockets in the system using fpocket and mdpocket and calculate their volume along the trajectory, using a sampling of frames. The analysis is skipped if there are atoms under periodic boundary conditions.

    Args:
        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).
        output_analysis_filepath (str): Pockets analysis results. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_pockets.json>`_. Accepted formats: json (edam:format_3464).
        output_pockets_zip_path (str) (Optional): Zip file with the structure of every pocket. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dic):
            * **pbc_selection** (*str*) - (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
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

            from biobb_mddb.workflow.pockets import pockets

            prop = {}
            pockets(input_topology_filepath='/path/to/topology.prmtop',
                    input_structure_filepath='/path/to/structure.cif',
                    input_trajectory_filepath='/path/to/trajectory.xtc',
                    output_analysis_filepath='/path/to/pockets.json',
                    output_pockets_zip_path='/path/to/pockets_pockets.zip',
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
    flag = 'pockets'
    outputs = {
        'output_analysis_filepath': ('file', 'mda.pockets.json'),
        'output_pockets_zip_path': ('glob', 'mdf.pocket*'),
    }
    input_fields = {'pbc_selection': 'pbc_selection'}

    def __init__(self, input_topology_filepath: str,
                 input_structure_filepath: str,
                 input_trajectory_filepath: str,
                 output_analysis_filepath: str,
                 input_inputs_filepath: str | None = None,
                 output_pockets_zip_path: str | None = None,
                 properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())


pockets = launcher(Pockets)


if __name__ == '__main__':
    Pockets.main()
