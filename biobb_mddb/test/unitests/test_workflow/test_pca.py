from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.pca import pca


class TestPca():
    def setup_class(self):
        fx.test_setup(self, 'pca')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_pca(self):
        returncode = pca(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.not_empty(self.paths['output_projections_zip_path'])
        assert fx.exe_success(returncode)
