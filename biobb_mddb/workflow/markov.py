#!/usr/bin/env python3

"""Module containing the Markov class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis


class Markov(MddbAnalysis):
    """
    | biobb_mddb Markov
    | Wrapper of the `Markov State Model analysis from MDDB workflow <https://github.com/mmb-irb/MDDB-workflow/blob/master/mddb_workflow/analyses/markov.py>`_ module.
    | Find the most populated frames of a Markov State Model (MSM) and calculate the RMSD matrix between them.

    Args:
        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).
        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif>`_. Accepted formats: cif (edam:format_1477).
        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc>`_. Accepted formats: xtc (edam:format_3875).
        input_populations_filepath (str): JSON file with the list of Markov State Model equilibrium populations, one per frame. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/populations.json>`_. Accepted formats: json (edam:format_3464).
        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).
        output_analysis_filepath (str): Markov analysis results. File type: output. `Sample file <https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_markov.json>`_. Accepted formats: json (edam:format_3464).
        output_screenshots_zip_path (str) (Optional): Zip file with the screenshots of the most populated frames. File type: output. Accepted formats: zip (edam:format_3987).
        properties (dic):
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

            from biobb_mddb.workflow.markov import markov

            prop = {}
            markov(input_topology_filepath='/path/to/topology.prmtop',
                   input_structure_filepath='/path/to/structure.cif',
                   input_trajectory_filepath='/path/to/trajectory.xtc',
                   input_populations_filepath='/path/to/populations.json',
                   output_analysis_filepath='/path/to/markov.json',
                   output_screenshots_zip_path='/path/to/markov_screenshots.zip',
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
    flag = 'markov'
    outputs = {
        'output_analysis_filepath': ('file', 'mda.markov.json'),
        'output_screenshots_zip_path': ('glob', 'markov_screenshot_*.jpg'),
    }
    input_fields = {'cg_selection': 'cg_selection'}
    cli_inputs = {'input_populations_filepath': '-pop'}

    def __init__(self, input_topology_filepath: str,
                 input_structure_filepath: str,
                 input_trajectory_filepath: str,
                 input_populations_filepath: str,
                 output_analysis_filepath: str,
                 input_inputs_filepath: str | None = None,
                 output_screenshots_zip_path: str | None = None,
                 properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())


def markov(input_topology_filepath: str,
           input_structure_filepath: str,
           input_trajectory_filepath: str,
           input_populations_filepath: str,
           output_analysis_filepath: str,
           input_inputs_filepath: str | None = None,
           output_screenshots_zip_path: str | None = None,
           properties: dict | None = None, **kwargs) -> int:
    """Create :class:`Markov <workflow.markov.Markov>` class and
    execute the :meth:`launch() <workflow.markov.Markov.launch>` method."""
    return Markov(**dict(locals())).launch()


markov.__doc__ = Markov.__doc__
main = Markov.get_main(markov, 'Data to represent a Markov State Model (MSM).')


if __name__ == '__main__':
    main()
