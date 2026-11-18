from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.rmsf import rmsf


class TestRmsf():
    def setup_class(self):
        fx.test_setup(self, 'rmsf')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_rmsf(self):
        returncode = rmsf(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.equal(self.paths['output_analysis_filepath'], self.paths['ref_output_analysis_filepath'])
        assert fx.exe_success(returncode)
