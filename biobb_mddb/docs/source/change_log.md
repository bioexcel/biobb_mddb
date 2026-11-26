# Biobb MDDB changelog

## [Unreleased]

### Added

- New building blocks wrapping every MDDB workflow analysis: `rmsds`, `tmscores`, `rmsf`, `rgyr`, `pca`, `rmsd_pairwise`, `clusters`, `distance_per_residue`, `hydrogen_bonds`, `sasa`, `energies`, `dihedral_energies`, `pockets`, `helical_parameters`, `markov`, `membrane_density`, `membrane_thickness`, `area_per_lipid`, `lipid_order`, `lipid_interactions` and `membrane_channels`.
- Optional MDDB workflow inputs file (`input_inputs_filepath`) in every analysis block, to set interactions, ligands, atom selections, etc.

### Changed

- Analysis blocks share a common base class (`workflow/common.py`) and expect the processed mmCIF structure (`.cif`) written by current MDDB workflow versions.
- `input_processing` writes the output structure in mmCIF format.
- `input_processing` runs the workflow like the analysis blocks: an input topology named like the processed one (`topology.*`) no longer makes it fail, and paths with spaces or a `filter` selection with quotes are passed correctly.
- With `disable_sandbox`, the blocks remove what the workflow added to the working directory and nothing else.

### Fixed

- `input_processing` passed `-fit` when `filter` was set instead of `fit`.
- The documented default of `container_shell_path` was `/bin/bash` instead of `/bin/bash -c`.

## What's new in version [5.2.0](https://github.com/bioexcel/biobb_mddb/releases/tag/v5.2.0)?

### New features

* [UPDATE] New package with RMSD per residue analysis