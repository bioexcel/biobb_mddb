from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.helical_parameters import helical_parameters


class TestHelicalParameters():
    def setup_class(self):
        fx.test_setup(self, 'helical_parameters')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_helical_parameters(self):
        returncode = helical_parameters(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_zip_path'])
        assert fx.exe_success(returncode)
