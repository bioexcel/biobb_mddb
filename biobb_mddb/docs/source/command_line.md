# BioBB MDDB Command Line Help
Generic usage:
```python
biobb_command [-h] --config CONFIG --input_file(s) <input_file(s)> --output_file <output_file>
```
-----------------


## Area_per_lipid
Wrapper of the Membrane area per lipid analysis from MDDB workflow module.
### Get help
Command:
```python
area_per_lipid -h
```
    usage: area_per_lipid [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Area per lipid of the membrane.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Area per lipid analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_topology.tpr). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_inputs.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Area per lipid analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_area_per_lipid.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_area_per_lipid.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
area_per_lipid --config config_area_per_lipid.yml --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_area_per_lipid.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_area_per_lipid.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
area_per_lipid --config config_area_per_lipid.json --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_area_per_lipid.json
```

## Clusters
Wrapper of the Clusters analysis from MDDB workflow module.
### Get help
Command:
```python
clusters -h
```
    usage: clusters [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_ZIP_PATH
    
    Conformational clustering of every interaction.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_ZIP_PATH, --output_analysis_zip_path OUTPUT_ANALYSIS_ZIP_PATH
                            Zip file with the analysis summary (mda.clusters.json), one results file per interaction and the cluster screenshots. Accepted formats: zip.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_zip_path** (*string*): Zip file with the analysis summary (mda.clusters.json), one results file per interaction and the cluster screenshots. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **cg_selection** (*string*): (None) Atom selection (VMD syntax) of Coarse Grained beads. Use 'auto' to guess them. If not set, the value in the inputs file is used, or none by default.
* **interactions** (*array*): (None) List of interactions to be analyzed. Each interaction is a dictionary with the fields name, agent_1, selection_1, agent_2, selection_2 and optionally distance_cutoff (Å). Selections are in VMD syntax. If not set, interactions in the inputs file are used.
* **md_type** (*string*): (None) Type of molecular dynamics. If not set, the value in the inputs file is used, or 'trajectory' by default. 
* **framestep** (*number*): (None) Time between consecutive frames in nanoseconds (ns). If not set, the value in the inputs file is used.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_clusters.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
clusters --config config_clusters.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_clusters.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
clusters --config config_clusters.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```

## Dihedral_energies
Wrapper of the Dihedral energies analysis from MDDB workflow module.
### Get help
Command:
```python
dihedral_energies -h
```
    usage: dihedral_energies [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Torsion and energy of every dihedral along the trajectory.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Dihedral energies analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Dihedral energies analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_dihedral_energies.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_dihedral_energies.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
dihedral_energies --config config_dihedral_energies.yml --input_topology_filepath dna_topology.prmtop --input_structure_filepath dna_structure.cif --input_trajectory_filepath dna_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_dihedral_energies.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_dihedral_energies.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
dihedral_energies --config config_dihedral_energies.json --input_topology_filepath dna_topology.prmtop --input_structure_filepath dna_structure.cif --input_trajectory_filepath dna_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_dihedral_energies.json
```

## Distance_per_residue
Wrapper of the Distance per residue analysis from MDDB workflow module.
### Get help
Command:
```python
distance_per_residue -h
```
    usage: distance_per_residue [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_ZIP_PATH
    
    Average and standard deviation of the distance between interface residues.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_ZIP_PATH, --output_analysis_zip_path OUTPUT_ANALYSIS_ZIP_PATH
                            Zip file with the analysis summary (mda.dist_perres.json) and one results file per interaction. Accepted formats: zip.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_zip_path** (*string*): Zip file with the analysis summary (mda.dist_perres.json) and one results file per interaction. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **interactions** (*array*): (None) List of interactions to be analyzed. Each interaction is a dictionary with the fields name, agent_1, selection_1, agent_2, selection_2 and optionally distance_cutoff (Å). Selections are in VMD syntax. If not set, interactions in the inputs file are used.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_distance_per_residue.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
distance_per_residue --config config_distance_per_residue.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_distance_per_residue.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
distance_per_residue --config config_distance_per_residue.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```

## Energies
Wrapper of the Energies analysis from MDDB workflow module.
### Get help
Command:
```python
energies -h
```
    usage: energies [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_ZIP_PATH
    
    Electrostatic and van der Waals energies in the interface of every interaction.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_ZIP_PATH, --output_analysis_zip_path OUTPUT_ANALYSIS_ZIP_PATH
                            Zip file with the analysis summary (mda.energies.json) and one results file per interaction. Accepted formats: zip.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_zip_path** (*string*): Zip file with the analysis summary (mda.energies.json) and one results file per interaction. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cg_selection** (*string*): (None) Atom selection (VMD syntax) of Coarse Grained beads. Use 'auto' to guess them. If not set, the value in the inputs file is used, or none by default.
* **interactions** (*array*): (None) List of interactions to be analyzed. Each interaction is a dictionary with the fields name, agent_1, selection_1, agent_2, selection_2 and optionally distance_cutoff (Å). Selections are in VMD syntax. If not set, interactions in the inputs file are used.
* **energies_engine** (*string*): (cmip) Engine used to calculate the energies. 
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_energies.yml)
```python
properties:
  energies_engine: gridfree
  remove_tmp: true

```
#### Command line
```python
energies --config config_energies.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_energies.json)
```python
{
  "properties": {
    "remove_tmp": true,
    "energies_engine": "gridfree"
  }
}
```
#### Command line
```python
energies --config config_energies.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```

## Helical_parameters
Wrapper of the Helical parameters analysis from MDDB workflow module.
### Get help
Command:
```python
helical_parameters -h
```
    usage: helical_parameters [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_ZIP_PATH
    
    Helical parameters of nucleic acids.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_ZIP_PATH, --output_analysis_zip_path OUTPUT_ANALYSIS_ZIP_PATH
                            Zip file with all helical parameters analysis results. Accepted formats: zip.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/dna_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_zip_path** (*string*): Zip file with all helical parameters analysis results. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_helical_parameters.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
helical_parameters --config config_helical_parameters.yml --input_topology_filepath dna_topology.prmtop --input_structure_filepath dna_structure.cif --input_trajectory_filepath dna_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_helical_parameters.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
helical_parameters --config config_helical_parameters.json --input_topology_filepath dna_topology.prmtop --input_structure_filepath dna_structure.cif --input_trajectory_filepath dna_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```

## Hydrogen_bonds
Wrapper of the Hydrogen bonds analysis from MDDB workflow module.
### Get help
Command:
```python
hydrogen_bonds -h
```
    usage: hydrogen_bonds [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_ZIP_PATH
    
    Hydrogen bonds in the interface of every interaction.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_ZIP_PATH, --output_analysis_zip_path OUTPUT_ANALYSIS_ZIP_PATH
                            Zip file with the analysis summary (mda.hbonds.json) and one results file per interaction. Accepted formats: zip.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_zip_path** (*string*): Zip file with the analysis summary (mda.hbonds.json) and one results file per interaction. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **interactions** (*array*): (None) List of interactions to be analyzed. Each interaction is a dictionary with the fields name, agent_1, selection_1, agent_2, selection_2 and optionally distance_cutoff (Å). Selections are in VMD syntax. If not set, interactions in the inputs file are used.
* **md_type** (*string*): (None) Type of molecular dynamics. If not set, the value in the inputs file is used, or 'trajectory' by default. 
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_hydrogen_bonds.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
hydrogen_bonds --config config_hydrogen_bonds.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_hydrogen_bonds.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
hydrogen_bonds --config config_hydrogen_bonds.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```

## Input_processing
Wrapper of the Input processing steps from MDDB workflow module.
### Get help
Command:
```python
input_processing -h
```
    usage: input_processing [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH --output_topology_filepath OUTPUT_TOPOLOGY_FILEPATH --output_trajectory_filepath OUTPUT_TRAJECTORY_FILEPATH --output_structure_filepath OUTPUT_STRUCTURE_FILEPATH
    
    Process raw input files using the MDDB workflow.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Input topology or structure file. Accepted formats: pdb, gro, prmtop, top, itp, tpr, psf.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Input trajectory file. Accepted formats: xtc, trr, dcd, nc.
      --output_topology_filepath OUTPUT_TOPOLOGY_FILEPATH
                            Output topology file, with a filtered set of atoms matching the trajectory. Accepted formats: prmtop, top, tpr, psf.
      --output_trajectory_filepath OUTPUT_TRAJECTORY_FILEPATH
                            Output XTC trajectory file with the filtered, imaged and fitted coordinates. Accepted formats: xtc.
      --output_structure_filepath OUTPUT_STRUCTURE_FILEPATH
                            Output mmCIF structure file with the filtered, imaged and fitted coordinates. Accepted formats: cif.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Input topology or structure file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/input_topology.top). Accepted formats: PDB, GRO, PRMTOP, TOP, ITP, TPR, PSF
* **input_trajectory_filepath** (*string*): Input trajectory file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/input_trajectory.dcd). Accepted formats: XTC, TRR, DCD, NC
* **output_topology_filepath** (*string*): Output topology file, with a filtered set of atoms matching the trajectory. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **output_trajectory_filepath** (*string*): Output XTC trajectory file with the filtered, imaged and fitted coordinates. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **output_structure_filepath** (*string*): Output mmCIF structure file with the filtered, imaged and fitted coordinates. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **filter** (*string*): (False) Removed atoms from the system. A custom atom selection may be passed using VMD selection syntax. Pass the label 'def' to remove water and counter ions by default
* **image** (*boolean*): (False) Set if the workflow must attempt to automatically image the system (remove Periodic Boundary Conditions where pertinent). WARNING: This is a simple default imaging protocol and may fail in many cases.
* **fit** (*boolean*): (False) Set if the workflow must attempt to automatically fit the system (remove rotation and translation where pertinent).
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_input_processing.yml)
```python
properties:
  filter: false
  fit: false
  image: false
  remove_tmp: true

```
#### Command line
```python
input_processing --config config_input_processing.yml --input_topology_filepath input_topology.top --input_trajectory_filepath input_trajectory.dcd --output_topology_filepath output_topology.prmtop --output_trajectory_filepath output_trajectory.xtc --output_structure_filepath output_structure.cif
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_input_processing.json)
```python
{
  "properties": {
    "filter": false,
    "image": false,
    "fit": false,
    "remove_tmp": true
  }
}
```
#### Command line
```python
input_processing --config config_input_processing.json --input_topology_filepath input_topology.top --input_trajectory_filepath input_trajectory.dcd --output_topology_filepath output_topology.prmtop --output_trajectory_filepath output_trajectory.xtc --output_structure_filepath output_structure.cif
```

## Lipid_interactions
Wrapper of the Membrane lipid-protein interactions analysis from MDDB workflow module.
### Get help
Command:
```python
lipid_interactions -h
```
    usage: lipid_interactions [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Contacts between lipids and other residues.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Lipid-protein interactions analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_topology.tpr). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_inputs.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Lipid-protein interactions analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_lipid_interactions.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_lipid_interactions.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
lipid_interactions --config config_lipid_interactions.yml --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_lipid_interactions.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_lipid_interactions.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
lipid_interactions --config config_lipid_interactions.json --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_lipid_interactions.json
```

## Lipid_order
Wrapper of the Membrane lipid order analysis from MDDB workflow module.
### Get help
Command:
```python
lipid_order -h
```
    usage: lipid_order [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Lipid tail order parameters.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Lipid order analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_topology.tpr). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_inputs.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Lipid order analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_lipid_order.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_lipid_order.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
lipid_order --config config_lipid_order.yml --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_lipid_order.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_lipid_order.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
lipid_order --config config_lipid_order.json --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_lipid_order.json
```

## Markov
Wrapper of the Markov State Model analysis from MDDB workflow module.
### Get help
Command:
```python
markov -h
```
    usage: markov [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH --input_populations_filepath INPUT_POPULATIONS_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH [--output_screenshots_zip_path OUTPUT_SCREENSHOTS_ZIP_PATH]
    
    Data to represent a Markov State Model (MSM).
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      --input_populations_filepath INPUT_POPULATIONS_FILEPATH
                            JSON file with the list of Markov State Model equilibrium populations, one per frame. Accepted formats: json.
      --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Markov analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
      --output_screenshots_zip_path OUTPUT_SCREENSHOTS_ZIP_PATH
                            Zip file with the screenshots of the most populated frames. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_populations_filepath** (*string*): JSON file with the list of Markov State Model equilibrium populations, one per frame. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/populations.json). Accepted formats: JSON
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Markov analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_markov.json). Accepted formats: JSON
* **output_screenshots_zip_path** (*string*): Zip file with the screenshots of the most populated frames. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **cg_selection** (*string*): (None) Atom selection (VMD syntax) of Coarse Grained beads. Use 'auto' to guess them. If not set, the value in the inputs file is used, or none by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_markov.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
markov --config config_markov.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_populations_filepath populations.json --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_markov.json --output_screenshots_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_markov.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
markov --config config_markov.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_populations_filepath populations.json --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_markov.json --output_screenshots_zip_path output.zip
```

## Membrane_channels
Wrapper of the Membrane channels analysis from MDDB workflow module.
### Get help
Command:
```python
membrane_channels -h
```
    usage: membrane_channels [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Channels across the membrane.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Membrane channels analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/channel_topology.tpr). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/channel_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/channel_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_inputs.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Membrane channels analysis results. File type: output. [Sample file](None). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_membrane_channels.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
membrane_channels --config config_membrane_channels.yml --input_topology_filepath channel_topology.tpr --input_structure_filepath channel_structure.cif --input_trajectory_filepath channel_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath output.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_membrane_channels.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
membrane_channels --config config_membrane_channels.json --input_topology_filepath channel_topology.tpr --input_structure_filepath channel_structure.cif --input_trajectory_filepath channel_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath output.json
```

## Membrane_density
Wrapper of the Membrane density analysis from MDDB workflow module.
### Get help
Command:
```python
membrane_density -h
```
    usage: membrane_density [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Density profile of membrane components along the membrane normal.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Membrane density analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_topology.tpr). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_inputs.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Membrane density analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_membrane_density.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_membrane_density.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
membrane_density --config config_membrane_density.yml --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_membrane_density.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_membrane_density.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
membrane_density --config config_membrane_density.json --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_membrane_density.json
```

## Membrane_thickness
Wrapper of the Membrane thickness analysis from MDDB workflow module.
### Get help
Command:
```python
membrane_thickness -h
```
    usage: membrane_thickness [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Membrane thickness along the trajectory.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Membrane thickness analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_topology.tpr). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/membrane_inputs.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Membrane thickness analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_membrane_thickness.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_membrane_thickness.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
membrane_thickness --config config_membrane_thickness.yml --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_membrane_thickness.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_membrane_thickness.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
membrane_thickness --config config_membrane_thickness.json --input_topology_filepath membrane_topology.tpr --input_structure_filepath membrane_structure.cif --input_trajectory_filepath membrane_trajectory.xtc --input_inputs_filepath membrane_inputs.json --output_analysis_filepath ref_membrane_thickness.json
```

## Pca
Wrapper of the Principal component analysis from MDDB workflow module.
### Get help
Command:
```python
pca -h
```
    usage: pca [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH [--output_projections_zip_path OUTPUT_PROJECTIONS_ZIP_PATH]
    
    Principal component analysis (PCA) of the trajectory.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            PCA analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
      --output_projections_zip_path OUTPUT_PROJECTIONS_ZIP_PATH
                            Zip file with the trajectory projections over each principal component, in XTC format. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): PCA analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_pca.json). Accepted formats: JSON
* **output_projections_zip_path** (*string*): Zip file with the trajectory projections over each principal component, in XTC format. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **pca_fit_selection** (*string*): (None) Atom selection (VMD syntax) for the fitting before the PCA. If not set, the workflow default is used: protein and nucleic acid backbone.
* **pca_analysis_selection** (*string*): (None) Atom selection (VMD syntax) for the PCA. If not set, the workflow default is used: protein and nucleic acid backbone.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_pca.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
pca --config config_pca.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_pca.json --output_projections_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_pca.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
pca --config config_pca.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_pca.json --output_projections_zip_path output.zip
```

## Pockets
Wrapper of the Pockets analysis from MDDB workflow module.
### Get help
Command:
```python
pockets -h
```
    usage: pockets [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH [--output_pockets_zip_path OUTPUT_POCKETS_ZIP_PATH]
    
    Pockets and their volume along the trajectory.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Pockets analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
      --output_pockets_zip_path OUTPUT_POCKETS_ZIP_PATH
                            Zip file with the structure of every pocket. Accepted formats: zip.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Pockets analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_pockets.json). Accepted formats: JSON
* **output_pockets_zip_path** (*string*): Zip file with the structure of every pocket. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_pockets.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
pockets --config config_pockets.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_pockets.json --output_pockets_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_pockets.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
pockets --config config_pockets.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_pockets.json --output_pockets_zip_path output.zip
```

## Rgyr
Wrapper of the Radius of gyration analysis from MDDB workflow module.
### Get help
Command:
```python
rgyr -h
```
    usage: rgyr [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Radius of gyration along the trajectory.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Radius of gyration analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Radius of gyration analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_rgyr.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rgyr.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
rgyr --config config_rgyr.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rgyr.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rgyr.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
rgyr --config config_rgyr.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rgyr.json
```

## Rmsd_pairwise
Wrapper of the RMSD pairwise analysis from MDDB workflow module.
### Get help
Command:
```python
rmsd_pairwise -h
```
    usage: rmsd_pairwise [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_ZIP_PATH
    
    RMSD between every pair of frames.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_ZIP_PATH, --output_analysis_zip_path OUTPUT_ANALYSIS_ZIP_PATH
                            Zip file with the analysis summary (mda.rmsd_pairwise.json) and one results file per analyzed selection. Accepted formats: zip.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_zip_path** (*string*): Zip file with the analysis summary (mda.rmsd_pairwise.json) and one results file per analyzed selection. File type: output. [Sample file](None). Accepted formats: ZIP
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **interactions** (*array*): (None) List of interactions to be analyzed. Each interaction is a dictionary with the fields name, agent_1, selection_1, agent_2, selection_2 and optionally distance_cutoff (Å). Selections are in VMD syntax. If not set, interactions in the inputs file are used.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_pairwise.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
rmsd_pairwise --config config_rmsd_pairwise.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_pairwise.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
rmsd_pairwise --config config_rmsd_pairwise.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_zip_path output.zip
```

## Rmsd_per_residue
Wrapper of the RMSD per residue analysis from MDDB workflow module.
### Get help
Command:
```python
rmsd_per_residue -h
```
    usage: rmsd_per_residue [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Average and standard deviation of the RMSD per residue.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            RMSD per residue analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): RMSD per residue analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_rmsd_per_residue.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_per_residue.yml)
```python
properties:
  remove_tmp: true

```
#### [Docker config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_per_residue_docker.yml)
```python
properties:
  container_image: ghcr.io/mmb-irb/mddb_wf:latest
  container_path: docker
  container_user_id: '1001'
  remove_tmp: true

```
#### Command line
```python
rmsd_per_residue --config config_rmsd_per_residue.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rmsd_per_residue.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_per_residue.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### [Docker config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsd_per_residue_docker.json)
```python
{
  "properties": {
    "remove_tmp": true,
    "container_path": "docker",
    "container_image": "ghcr.io/mmb-irb/mddb_wf:latest",
    "container_user_id": "1001"
  }
}
```
#### Command line
```python
rmsd_per_residue --config config_rmsd_per_residue.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rmsd_per_residue.json
```

## Rmsds
Wrapper of the RMSDs analysis from MDDB workflow module.
### Get help
Command:
```python
rmsds -h
```
    usage: rmsds [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    RMSD along the trajectory against the first frame and the average structure.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            RMSDs analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): RMSDs analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_rmsds.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **cg_selection** (*string*): (None) Atom selection (VMD syntax) of Coarse Grained beads. Use 'auto' to guess them. If not set, the value in the inputs file is used, or none by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsds.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
rmsds --config config_rmsds.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rmsds.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsds.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
rmsds --config config_rmsds.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rmsds.json
```

## Rmsf
Wrapper of the Fluctuation analysis from MDDB workflow module.
### Get help
Command:
```python
rmsf -h
```
    usage: rmsf [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    RMSF, the fluctuation of every atom along the trajectory.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            Fluctuation analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): Fluctuation analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_rmsf.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsf.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
rmsf --config config_rmsf.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rmsf.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_rmsf.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
rmsf --config config_rmsf.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_rmsf.json
```

## Sasa
Wrapper of the Solvent accessible surface analysis from MDDB workflow module.
### Get help
Command:
```python
sasa -h
```
    usage: sasa [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    Solvent accessible surface area (SASA) per residue.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            SASA analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): SASA analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_sasa.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_sasa.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
sasa --config config_sasa.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_sasa.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_sasa.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
sasa --config config_sasa.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_sasa.json
```

## Tmscores
Wrapper of the TM scores analysis from MDDB workflow module.
### Get help
Command:
```python
tmscores -h
```
    usage: tmscores [-h] [-c CONFIG] --input_topology_filepath INPUT_TOPOLOGY_FILEPATH --input_structure_filepath INPUT_STRUCTURE_FILEPATH --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH [--input_inputs_filepath INPUT_INPUTS_FILEPATH] -o OUTPUT_ANALYSIS_FILEPATH
    
    TM scores along the trajectory against the first frame and the average structure.
    
    options:
      -h, --help            show this help message and exit
      -c CONFIG, --config CONFIG
                            This file can be a YAML file, JSON file or JSON string
    
    required arguments:
      --input_topology_filepath INPUT_TOPOLOGY_FILEPATH
                            Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: prmtop, top, tpr, psf.
      --input_structure_filepath INPUT_STRUCTURE_FILEPATH
                            Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). Accepted formats: cif.
      --input_trajectory_filepath INPUT_TRAJECTORY_FILEPATH
                            Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). Accepted formats: xtc.
      -o OUTPUT_ANALYSIS_FILEPATH, --output_analysis_filepath OUTPUT_ANALYSIS_FILEPATH
                            TM scores analysis results. Accepted formats: json.
    
    optional arguments:
      --input_inputs_filepath INPUT_INPUTS_FILEPATH
                            MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. Accepted formats: json, yaml, yml.
### I / O Arguments
Syntax: input_argument (datatype) : Definition

Config input / output arguments for this building block:
* **input_topology_filepath** (*string*): Already processed topology file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_topology.prmtop). Accepted formats: PRMTOP, TOP, TPR, PSF
* **input_structure_filepath** (*string*): Already processed mmCIF structure file, with atoms matching the trajectory (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_structure.cif). Accepted formats: CIF
* **input_trajectory_filepath** (*string*): Already processed XTC trajectory file, with imaged and fitted coordinates (e.g. the output of the input processing block). File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/output_trajectory.xtc). Accepted formats: XTC
* **input_inputs_filepath** (*string*): MDDB workflow inputs file, to set analysis parameters such as interactions, ligands or atom selections. Properties have priority over values in this file. File type: input. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/data/workflow/inputs_interactions.json). Accepted formats: JSON, YAML, YML
* **output_analysis_filepath** (*string*): TM scores analysis results. File type: output. [Sample file](https://github.com/bioexcel/biobb_mddb/raw/master/biobb_mddb/test/reference/workflow/ref_tmscores.json). Accepted formats: JSON
### Config
Syntax: input_parameter (datatype) - (default_value) Definition

Config parameters for this building block:
* **pbc_selection** (*string*): (None) Atom selection (VMD syntax) of atoms under Periodic Boundary Conditions (e.g. solvent, ions, membrane lipids), which are excluded from the analysis. Use 'auto' to guess them. If not set, the value in the inputs file is used, or 'auto' by default.
* **binary_path** (*string*): (mwf) Path to the MDDB workflow executable binary.
* **remove_tmp** (*boolean*): (True) Remove temporal files.
* **restart** (*boolean*): (False) Do not execute if output files exist.
* **sandbox_path** (*string*): (./) Parent path to the sandbox directory.
* **container_path** (*string*): (None) Path to the binary executable of your container.
* **container_image** (*string*): (ghcr.io/mmb-irb/mddb_wf:latest) Container Image identifier.
* **container_volume_path** (*string*): (/data) Path to an internal directory in the container.
* **container_user_id** (*string*): (None) User number id to be mapped inside the container.
* **container_shell_path** (*string*): (/bin/bash -c) Path to the binary executable of the container shell.
### YAML
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_tmscores.yml)
```python
properties:
  remove_tmp: true

```
#### Command line
```python
tmscores --config config_tmscores.yml --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_tmscores.json
```
### JSON
#### [Common config file](https://github.com/bioexcel/biobb_mddb/blob/master/biobb_mddb/test/data/config/config_tmscores.json)
```python
{
  "properties": {
    "remove_tmp": true
  }
}
```
#### Command line
```python
tmscores --config config_tmscores.json --input_topology_filepath output_topology.prmtop --input_structure_filepath output_structure.cif --input_trajectory_filepath output_trajectory.xtc --input_inputs_filepath inputs_interactions.json --output_analysis_filepath ref_tmscores.json
```
