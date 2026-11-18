from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.pockets import pockets


class TestPockets():
    def setup_class(self):
        fx.test_setup(self, 'pockets')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_pockets(self):
        returncode = pockets(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.not_empty(self.paths['output_pockets_zip_path'])
        assert fx.exe_success(returncode)
