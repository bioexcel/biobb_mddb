from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.area_per_lipid import area_per_lipid


class TestAreaPerLipid():
    def setup_class(self):
        fx.test_setup(self, 'area_per_lipid')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_area_per_lipid(self):
        returncode = area_per_lipid(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.exe_success(returncode)
