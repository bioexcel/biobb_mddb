# biobb_mddb

BioBB wrappers of the MDDB workflow (`mwf`, repository in `~/libraries/workflow`).

## Generated building blocks

Every analysis block in `biobb_mddb/workflow/` except `input_processing.py` and `common.py` is generated. Do not edit them by hand:

- `utils/specs.py`: one entry per block (workflow flag, outputs, properties, test system, flags such as `nondeterministic`, `no_reference` or `standby`).
- `utils/generate.py`: writes the block modules, their tests (`test/unitests/test_workflow/test_<name>.py`) and the generated part of `test/conf.yml` (everything after `rmsds:`; entries before it are written by hand).
- `utils/make_refs.py <workdir> [--write-refs] <names>`: runs blocks with their `conf.yml` entry and compares outputs with references, or writes them.
- The shared logic (staging inputs, inputs file, collecting outputs, container command) is in `biobb_mddb/workflow/common.py`.

After changing specs: `python3 utils/generate.py`, then update `workflow/__init__.py`, `setup.py`, `docs/source/workflow.rst` and `json_schemas/biobb_mddb.json` if blocks were added or removed, and rerun the utils_biobb generators.

`allostery` and `chemical_shifts` are in stand by (Compass and LEGOLAS are not fully integrated in the workflow): their modules and tests exist but tests are skipped and they are not registered in `__init__`, `setup.py`, docs or `biobb_mddb.json`.

## Derived files (utils_biobb)

`json_schemas/*.json`, `test/data/config/*` and `docs/source/command_line.md` are generated with https://github.com/bioexcel/utils_biobb from `utils_biobb/utils_biobb` with `PYTHONPATH` set to the utils_biobb repo root. The package must be installed in editable mode (`pip install -e . --no-deps`) so console scripts exist:

```
python3 json/json_generator.py -p biobb_mddb -o <repo>/biobb_mddb/
python3 json/json_validator.py -p biobb_mddb -i <repo>/biobb_mddb/json_schemas/ -s json/schema/master_schema.json
python3 configs/configs_generator.py -i <repo>/biobb_mddb/test/conf.yml -o <repo>/biobb_mddb/test/data/config/
python3 command_line/command_line_doc_generator.py -j <repo>/biobb_mddb/json_schemas/ -c <repo>/biobb_mddb/test/data/config/ -b biobb_mddb -o <repo>/biobb_mddb/docs/source/command_line.md
```

## Tests

- Activate the env with `conda activate mwf_env` (not just its `bin` in `PATH`): the patched `gmx_mddb` (with `gmx dump --json`) is only added to `PATH` by its activation script.
- Run from `biobb_mddb/test/unitests/test_workflow`. The full suite takes ~25 min (pockets ~15 min).
- Test systems in `test/data/workflow/`: protein (`output_*`), DNA `MD-A001LK` (`dna_*`), membrane `mmb-A01KI` (`membrane_*`), GABA(A) receptor channel `mmb-A01JD` (`channel_*`, processed with `-t stabonds`).
- The docker test uses `ghcr.io/mmb-irb/mddb_wf:latest`, built from `~/libraries/workflow/docker/Dockerfile`.
