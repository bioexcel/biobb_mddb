from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.markov import markov


class TestMarkov():
    def setup_class(self):
        fx.test_setup(self, 'markov')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_markov(self):
        returncode = markov(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.equal(self.paths['output_analysis_filepath'], self.paths['ref_output_analysis_filepath'])
        assert fx.not_empty(self.paths['output_screenshots_zip_path'])
        assert fx.exe_success(returncode)
