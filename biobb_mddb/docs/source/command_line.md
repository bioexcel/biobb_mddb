# BioBB MDDB Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Rmsd_per_residue
Calculate average and standard deviation RMSD per residue for every residue in a system using a sampling of frames along the trajectory.
### Get help
Command:
```python
rmsd_per_residue -h
```
    usage: rmsd_per_residue [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH -o OUTPUT_ANALYSIS_FILEPATH
    
    RMSD per residue using the MDDB workflow.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Input topology or structure file. Accepted formats: pdb, gro, prmtop, top, itp, tpr, psf.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Input trajectory file. Accepted formats: xtc, trr, dcd, nc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Analysis results file. Accepted formats: json.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Input topology or structure file. File type: input. [Sample file](https://urlto.sample). Accepted formats: PDB, GRO, PRMTOP, TOP, ITP, TPR, PSF
* **input_trajectory_filepath** (*string*): Input trajectory file. File type: input. [Sample file](https://urlto.sample). Accepted formats: XTC, TRR, DCD, NC
* **output_analysis_filepath** (*string*): Analysis results file. File type: output. [Sample file](https://urlto.sample). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **skip_processing** (*boolean*): (False) Do not process input files, assuming they were already processed.
* **binary_path** (*string*): (mwf) Example of executable binary property.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_per_residue.yml)
```python
properties:
  remove_tmp: true
  skip_processing: false

```
#### Command line
```python
rmsd_per_residue --config config_rmsd_per_residue.yml --input_topology_filepath urlto.sample --input_trajectory_filepath urlto.sample --output_analysis_filepath urlto.sample
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_per_residue.json)
```python
{
  "properties": {
    "skip_processing": false,
    "remove_tmp": true
  }
}
```
#### Command line
```python
rmsd_per_residue --config config_rmsd_per_residue.json --input_topology_filepath urlto.sample --input_trajectory_filepath urlto.sample --output_analysis_filepath urlto.sample
```
