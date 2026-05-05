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
    install_requires=['biobb_common==5.2.2'],
    python_requires='>=3.10',
    entry_points={
        "console_scripts": [
            "rmsd_per_residue = biobb_mddb.workflow.rmsd_per_residue:main"
        ]
    },
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix"
    ),
)
