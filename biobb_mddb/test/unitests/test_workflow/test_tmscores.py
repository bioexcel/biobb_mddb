from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.tmscores import tmscores


class TestTmscores():
    def setup_class(self):
        fx.test_setup(self, 'tmscores')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_tmscores(self):
        returncode = tmscores(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.exe_success(returncode)
