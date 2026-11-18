"""Run blocks from conf.yml once through biobb. With --write-refs, store reference outputs in test/reference/workflow."""
import sys, os, shutil, importlib, time, traceback
from pathlib import Path
import yaml

# Package directory (this file lives in <repo>/utils)
REPO = Path(__file__).resolve().parent.parent / 'biobb_mddb'
DATA = REPO / 'test' / 'data'
REF = REPO / 'test' / 'reference'
WORK = Path(sys.argv[1])
write_refs = '--write-refs' in sys.argv
names = [a for a in sys.argv[2:] if not a.startswith('--')]
conf = yaml.safe_load(open(REPO / 'test' / 'conf.yml'))
for name in names:
    entry = conf[name]
    workdir = WORK / name
    shutil.rmtree(workdir, ignore_errors=True)
    workdir.mkdir(parents=True)
    os.chdir(workdir)
    paths = {}
    refs = {}
    for key, value in entry['paths'].items():
        value = value.replace('file:test_data_dir', str(DATA)).replace('file:test_reference_dir', str(REF))
        if key.startswith('ref_'): refs[key[4:]] = value
        else: paths[key] = value
    func = getattr(importlib.import_module(f'biobb_mddb.workflow.{name}'), name)
    start = time.time()
    try:
        code = func(properties=dict(entry.get('properties', {})), **paths)
    except Exception:
        print(f'{name}: FAILED after {time.time() - start:.0f}s', flush=True)
        traceback.print_exc()
        continue
    print(f'{name}: rc={code} in {time.time() - start:.0f}s', flush=True)
    for key, value in paths.items():
        if key.startswith('output_'):
            print(f'  {key}: {Path(value).stat().st_size if Path(value).exists() else "MISSING"} bytes', flush=True)
    for key, ref in refs.items():
        if write_refs:
            Path(ref).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(paths[key], ref)
            print(f'  ref written {ref}', flush=True)
        else:
            same = Path(ref).exists() and Path(ref).read_bytes() == Path(paths[key]).read_bytes()
            print(f'  {key} identical to reference: {same}', flush=True)
