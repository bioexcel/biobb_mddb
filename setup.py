import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="biobb_mddb",
    version="5.2.0",
    author="Biobb developers",
    author_email="your@email.com",
    description="Biobb_mddb is a set of tools to work with MD simulations for and from MDDB sources.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="Bioinformatics Workflows BioExcel Compatibility",
    url="https://github.com/bioexcel/biobb_mddb",
    project_urls={
        "Documentation": "http://biobb-mddb.readthedocs.io/en/latest/",
        "Bioexcel": "https://bioexcel.eu/"
    },
    packages=setuptools.find_packages(exclude=['docs', 'test']),
    package_data={'biobb_mddb': ['py.typed']},
    install_requires=['biobb_common==5.3.1'],
    python_requires='>=3.11',
    entry_points={
        "console_scripts": [
            "area_per_lipid = biobb_mddb.workflow.area_per_lipid:main",
            "clusters = biobb_mddb.workflow.clusters:main",
            "dihedral_energies = biobb_mddb.workflow.dihedral_energies:main",
            "distance_per_residue = biobb_mddb.workflow.distance_per_residue:main",
            "energies = biobb_mddb.workflow.energies:main",
            "helical_parameters = biobb_mddb.workflow.helical_parameters:main",
            "hydrogen_bonds = biobb_mddb.workflow.hydrogen_bonds:main",
            "input_processing = biobb_mddb.workflow.input_processing:main",
            "lipid_interactions = biobb_mddb.workflow.lipid_interactions:main",
            "lipid_order = biobb_mddb.workflow.lipid_order:main",
            "markov = biobb_mddb.workflow.markov:main",
            "membrane_channels = biobb_mddb.workflow.membrane_channels:main",
            "membrane_density = biobb_mddb.workflow.membrane_density:main",
            "membrane_thickness = biobb_mddb.workflow.membrane_thickness:main",
            "pca = biobb_mddb.workflow.pca:main",
            "pockets = biobb_mddb.workflow.pockets:main",
            "rgyr = biobb_mddb.workflow.rgyr:main",
            "rmsd_pairwise = biobb_mddb.workflow.rmsd_pairwise:main",
            "rmsd_per_residue = biobb_mddb.workflow.rmsd_per_residue:main",
            "rmsds = biobb_mddb.workflow.rmsds:main",
            "rmsf = biobb_mddb.workflow.rmsf:main",
            "sasa = biobb_mddb.workflow.sasa:main",
            "tmscores = biobb_mddb.workflow.tmscores:main"
        ]
    },
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix"
    ),
)
