from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.energies import energies


class TestEnergies():
    def setup_class(self):
        fx.test_setup(self, 'energies')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_energies(self):
        returncode = energies(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_zip_path'])
        assert fx.exe_success(returncode)
