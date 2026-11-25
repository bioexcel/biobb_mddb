#!/usr/bin/env python3

"""Module containing the Rmsds class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis


class Rmsds(MddbAnalysis):
    """
    | biobb_mddb Rmsds
    | Wrapper of the `RMSDs analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/rmsds.py>`_ module.
    | Calculate the RMSD of every frame along the trajectory against the first frame and against the average structure for several atom selections (e.g. protein, nucleic acids, ligands).

    Args:
        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).
        output_analysis_filepath (str): RMSDs analysis results. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_rmsds.json>`_. Accepted formats: json (edam:format_3464).
        properties (dic):
            * **pbc_selection** (*str*) - (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
            * **cg_selection** (*str*) - (None) Atom selection (VMD syntax) of Coarse Grained beads. Use 'auto' to guess them. If not set, the value in the inputs file is used, or none by default.
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

            from biobb_mddb.workflow.rmsds import rmsds

            prop = {}
            rmsds(input_topology_filepath='/path/to/topology.prmtop',
                  input_structure_filepath='/path/to/structure.cif',
                  input_trajectory_filepath='/path/to/trajectory.xtc',
                  output_analysis_filepath='/path/to/rmsds.json',
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
    flag = 'rmsds'
    outputs = {
        'output_analysis_filepath': ('file', 'mda.rmsds.json'),
    }
    input_fields = {'pbc_selection': 'pbc_selection', 'cg_selection': 'cg_selection'}

    def __init__(self, input_topology_filepath: str,
                 input_structure_filepath: str,
                 input_trajectory_filepath: str,
                 output_analysis_filepath: str,
                 input_inputs_filepath: str | None = None,
                 properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())


def rmsds(input_topology_filepath: str,
          input_structure_filepath: str,
          input_trajectory_filepath: str,
          output_analysis_filepath: str,
          input_inputs_filepath: str | None = None,
          properties: dict | None = None, **kwargs) -> int:
    """Create :class:`Rmsds <workflow.rmsds.Rmsds>` class and
    execute the :meth:`launch() <workflow.rmsds.Rmsds.launch>` method."""
    return Rmsds(**dict(locals())).launch()


rmsds.__doc__ = Rmsds.__doc__
main = Rmsds.get_main(rmsds, 'RMSD along the trajectory against the first frame and the average structure.')


if __name__ == '__main__':
    main()
