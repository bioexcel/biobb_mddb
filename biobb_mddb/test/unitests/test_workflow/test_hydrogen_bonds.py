from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.hydrogen_bonds import hydrogen_bonds


class TestHydrogenBonds():
    def setup_class(self):
        fx.test_setup(self, 'hydrogen_bonds')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_hydrogen_bonds(self):
        returncode = hydrogen_bonds(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_zip_path'])
        assert fx.exe_success(returncode)
