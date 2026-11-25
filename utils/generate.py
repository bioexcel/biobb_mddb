"""Generate the MDDB workflow analysis building block modules, tests and conf.yml entries from specs.py."""
import sys
from pathlib import Path
from specs import SPECS, PROPS, INPUT_FIELDS, CLI_ARGS, WF_URL, SAMPLE, REFERENCE

# Repository root (this file lives in <repo>/utils)
REPO = Path(__file__).resolve().parent.parent
PKG = REPO / 'biobb_mddb'
# Blocks written by hand, whose conf.yml entries are kept before the generated ones
CONF_HEAD_END = '\nrmsds:'

WF_MODULES = {
    'membrane_density': 'density.py',
    'membrane_thickness': 'thickness.py',
    'membrane_channels': 'channels.py',
}

EDAM = {'json': 'json (edam:format_3464)', 'zip': 'zip (edam:format_3987)'}

COMMON_PROPS_TAIL = '''            * **binary_path** (*str*) - ("mwf") Path to the MDDB workflow executable binary.
            * **remove_tmp** (*bool*) - (True) [WF property] Remove temporal files.
            * **restart** (*bool*) - (False) [WF property] Do not execute if output files exist.
            * **sandbox_path** (*str*) - ("./") [WF property] Parent path to the sandbox directory.
            * **container_path** (*str*) - (None) Path to the binary executable of your container.
            * **container_image** (*str*) - ("ghcr.io/mmb-irb/mddb_wf:latest") Container Image identifier.
            * **container_volume_path** (*str*) - ("/data") Path to an internal directory in the container.
            * **container_working_dir** (*str*) - (None) Path to the internal CWD in the container.
            * **container_user_id** (*str*) - (None) User number id to be mapped inside the container.
            * **container_shell_path** (*str*) - ("/bin/bash") Path to the binary executable of the container shell.'''


def test_data_names(spec):
    """Input data files used by the test of this block."""
    system = spec.get('system', 'protein')
    if system == 'membrane':
        names = {
            'input_topology_filepath': 'membrane_topology.tpr',
            'input_structure_filepath': 'membrane_structure.cif',
            'input_trajectory_filepath': 'membrane_trajectory.xtc',
            'input_inputs_filepath': 'membrane_inputs.json',
        }
    elif system == 'channel':
        names = {
            'input_topology_filepath': 'channel_topology.tpr',
            'input_structure_filepath': 'channel_structure.cif',
            'input_trajectory_filepath': 'channel_trajectory.xtc',
            'input_inputs_filepath': 'membrane_inputs.json',
        }
    elif system == 'dna':
        names = {
            'input_topology_filepath': 'dna_topology.prmtop',
            'input_structure_filepath': 'dna_structure.cif',
            'input_trajectory_filepath': 'dna_trajectory.xtc',
        }
    else:
        names = {
            'input_topology_filepath': 'output_topology.prmtop',
            'input_structure_filepath': 'output_structure.cif',
            'input_trajectory_filepath': 'output_trajectory.xtc',
        }
    if spec.get('test_inputs'): names['input_inputs_filepath'] = 'inputs_interactions.json'
    if spec.get('populations'): names['input_populations_filepath'] = 'populations.json'
    return names


def reference_name(spec, output):
    key, otype, wf_filename, desc, ext = output
    return f'ref_{spec["name"]}{"_" + key.split("_")[1] if key != "output_analysis_filepath" and key != "output_analysis_zip_path" else ""}.{ext}'


def output_name(spec, output):
    key, otype, wf_filename, desc, ext = output
    if key in ('output_analysis_filepath', 'output_analysis_zip_path'): return f'{spec["name"]}.{ext}'
    return f'{spec["name"]}_{key.split("_")[1]}.{ext}'


def build_module(spec):
    name, cls, flag = spec['name'], spec['cls'], spec['flag']
    wf_module = WF_MODULES.get(name, spec['module'])
    data = test_data_names(spec)
    outputs = spec['outputs']
    props = spec['props']

    # --- Docstring arguments ---
    args = []
    args.append(f'        input_topology_filepath (str): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <{SAMPLE}/{data["input_topology_filepath"]}>`_. Accepted formats: prmtop (edam:format_3881), top (edam:format_3880), tpr (edam:format_2333), psf (edam:format_3882).')
    args.append(f'        input_structure_filepath (str): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. `Sample file <{SAMPLE}/{data["input_structure_filepath"]}>`_. Accepted formats: cif (edam:format_1477).')
    args.append(f'        input_trajectory_filepath (str): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. `Sample file <{SAMPLE}/{data["input_trajectory_filepath"]}>`_. Accepted formats: xtc (edam:format_3875).')
    if spec.get('populations'):
        args.append(f'        input_populations_filepath (str): JSON file with the list of Markov State Model equilibrium populations, one per frame. File type: input. `Sample file <{SAMPLE}/populations.json>`_. Accepted formats: json (edam:format_3464).')
    inputs_sample = data.get('input_inputs_filepath', 'inputs_interactions.json')
    args.append(f'        input_inputs_filepath (str) (Optional): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. `Sample file <{SAMPLE}/{inputs_sample}>`_. Accepted formats: json (edam:format_3464), yaml (edam:format_3750), yml (edam:format_3750).')
    for output in outputs:
        key, otype, wf_filename, desc, ext = output
        optional = ' (Optional)' if otype == 'glob' else ''
        # Only single file outputs have a reference file in the repository
        sample = f' `Sample file <{REFERENCE}/{reference_name(spec, output)}>`_.' if otype == 'file' and not spec.get('no_reference') else ''
        args.append(f'        {key} (str){optional}: {desc}. File type: output.{sample} Accepted formats: {EDAM[ext]}.')

    # --- Docstring properties ---
    prop_lines = [f'            {PROPS[p]}' for p in props]
    properties_doc = '\n'.join(prop_lines + [COMMON_PROPS_TAIL])

    # --- Example ---
    example_args = [f"input_topology_filepath='/path/to/topology.prmtop'",
                    f"input_structure_filepath='/path/to/structure.cif'",
                    f"input_trajectory_filepath='/path/to/trajectory.xtc'"]
    if spec.get('populations'): example_args.append("input_populations_filepath='/path/to/populations.json'")
    for output in outputs:
        example_args.append(f"{output[0]}='/path/to/{output_name(spec, output)}'")
    example_args.append('properties=prop')
    example_prop = '{}'
    if 'interactions' in props:
        example_prop = "{\n                'interactions': [{\n                    'name': 'protein-ligand interaction',\n                    'agent_1': 'protein', 'selection_1': 'protein',\n                    'agent_2': 'ligand', 'selection_2': 'resname LIG'\n                }]\n            }"
    joiner = ',\n' + ' ' * (12 + len(name) + 1)
    example = f'''            from biobb_mddb.workflow.{name} import {name}

            prop = {example_prop}
            {name}({joiner.join(example_args)})'''

    # --- Constructor ---
    in_keys = ['input_topology_filepath', 'input_structure_filepath', 'input_trajectory_filepath']
    if spec.get('populations'): in_keys.append('input_populations_filepath')
    in_keys.append('input_inputs_filepath')
    required_args = [k for k in in_keys if k != 'input_inputs_filepath'] + [o[0] for o in outputs if o[1] != 'glob']
    optional_args = ['input_inputs_filepath'] + [o[0] for o in outputs if o[1] == 'glob']
    signature_items = [f'{k}: str' for k in required_args] + [f'{k}: str | None = None' for k in optional_args]
    class_signature = (',\n' + ' ' * 17).join(signature_items)
    func_signature = (',\n' + ' ' * (len(name) + 5)).join(signature_items)

    # --- Class attributes ---
    outputs_attr = ',\n'.join(f"        '{o[0]}': ('{o[1]}', {o[2]!r})" for o in outputs)
    input_fields = {p: INPUT_FIELDS[p] for p in props if p in INPUT_FIELDS}
    cli_properties = {p: CLI_ARGS[p] for p in props if p in CLI_ARGS}
    class_attrs = f"    flag = '{flag}'\n    outputs = {{\n{outputs_attr},\n    }}\n"
    if input_fields: class_attrs += f'    input_fields = {input_fields!r}\n'
    if spec.get('input_defaults'): class_attrs += f"    input_defaults = {spec['input_defaults']!r}\n"
    if cli_properties: class_attrs += f'    cli_properties = {cli_properties!r}\n'
    if spec.get('populations'): class_attrs += "    cli_inputs = {'input_populations_filepath': '-pop'}\n"

    long_desc = spec['long']
    return f'''#!/usr/bin/env python3

"""Module containing the {cls} class and the command line interface."""
from biobb_mddb.workflow.common import MddbAnalysis


class {cls}(MddbAnalysis):
    """
    | biobb_mddb {cls}
    | Wrapper of the `{spec['title']} from MDDB workflow <{WF_URL}/{wf_module}>`_ module.
    | {long_desc}

    Args:
{chr(10).join(args)}
        properties (dic):
{properties_doc}

    Examples:
        This is a use example of how to use the building block from Python::

{example}

    Info:
        * wrapped_software:
            * name: MDDB Workflow
            * version: >=0.1.12
            * license: Apache-2.0
        * ontology:
            * name: EDAM
            * schema: http://edamontology.org/EDAM.owl

    """
{class_attrs}
    def __init__(self, {class_signature},
                 properties: dict | None = None, **kwargs) -> None:
        super().__init__(**locals())


def {name}({func_signature},
{' ' * (len(name) + 5)}properties: dict | None = None, **kwargs) -> int:
    """Create :class:`{cls} <workflow.{name}.{cls}>` class and
    execute the :meth:`launch() <workflow.{name}.{cls}.launch>` method."""
    return {cls}(**dict(locals())).launch()


{name}.__doc__ = {cls}.__doc__
main = {cls}.get_main({name}, '{spec['short']}')


if __name__ == '__main__':
    main()
'''


def build_test(spec):
    name, cls = spec['name'], spec['cls']
    lines = []
    for output in spec['outputs']:
        key = output[0]
        lines.append(f"        assert fx.not_empty(self.paths['{key}'])")
        # Some analyses are not deterministic (e.g. random seeds), so their outputs can not be compared
        if output[1] == 'file' and not spec.get('nondeterministic') and not spec.get('no_reference'):
            lines.append(f"        assert fx.equal(self.paths['{key}'], self.paths['ref_{key}'])")
    asserts = '\n'.join(lines)
    # Blocks in stand by are kept but their tests are skipped
    standby = spec.get('standby')
    header = 'import pytest\n' if standby else ''
    decorator = f"@pytest.mark.skip(reason='Stand by: {standby}')\n" if standby else ''
    return f'''{header}from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.{name} import {name}


{decorator}class Test{cls}():
    def setup_class(self):
        fx.test_setup(self, '{name}')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_{name}(self):
        returncode = {name}(properties=self.properties, **self.paths)
{asserts}
        assert fx.exe_success(returncode)
'''


def build_conf(spec):
    name = spec['name']
    data = test_data_names(spec)
    lines = [f'{name}:', '  paths:']
    for key, filename in data.items():
        lines.append(f'    {key}: file:test_data_dir/workflow/{filename}')
    for output in spec['outputs']:
        key = output[0]
        # Some outputs are too big or depend on the run (e.g. they include paths), so they have no reference
        if output[1] == 'file' and not spec.get('no_reference'):
            lines.append(f'    ref_{key}: file:test_reference_dir/workflow/{reference_name(spec, output)}')
        lines.append(f'    {key}: {output_name(spec, output)}')
    lines.append('  properties:')
    lines.append('    remove_tmp: true')
    for key, value in spec.get('test_props', {}).items():
        lines.append(f'    {key}: {value}')
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    # Optionally pass block names to regenerate only their modules and tests
    only = sys.argv[1:]
    for spec in SPECS:
        if only and spec['name'] not in only: continue
        (PKG / 'workflow' / f'{spec["name"]}.py').write_text(build_module(spec))
        (PKG / 'test' / 'unitests' / 'test_workflow' / f'test_{spec["name"]}.py').write_text(build_test(spec))
        print(spec['name'])
    # Rebuild the generated part of conf.yml, always with all blocks
    conf_filepath = PKG / 'test' / 'conf.yml'
    conf = conf_filepath.read_text()
    conf_head = conf[:conf.index(CONF_HEAD_END) + 1]
    conf_filepath.write_text(conf_head + '\n'.join(build_conf(spec) for spec in SPECS))
