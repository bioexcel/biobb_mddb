from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.membrane_density import membrane_density


class TestMembraneDensity():
    def setup_class(self):
        fx.test_setup(self, 'membrane_density')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_membrane_density(self):
        returncode = membrane_density(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.equal(self.paths['output_analysis_filepath'], self.paths['ref_output_analysis_filepath'])
        assert fx.exe_success(returncode)
