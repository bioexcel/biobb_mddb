from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.rmsds import rmsds


class TestRmsds():
    def setup_class(self):
        fx.test_setup(self, 'rmsds')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_rmsds(self):
        returncode = rmsds(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.equal(self.paths['output_analysis_filepath'], self.paths['ref_output_analysis_filepath'])
        assert fx.exe_success(returncode)
