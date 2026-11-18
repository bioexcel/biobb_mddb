import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.allostery import allostery


@pytest.mark.skip(reason='Stand by: Compass is not fully integrated in the MDDB workflow yet')
class TestAllostery():
    def setup_class(self):
        fx.test_setup(self, 'allostery')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_allostery(self):
        returncode = allostery(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.exe_success(returncode)
