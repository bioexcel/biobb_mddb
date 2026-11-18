from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.clusters import clusters


class TestClusters():
    def setup_class(self):
        fx.test_setup(self, 'clusters')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_clusters(self):
        returncode = clusters(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_zip_path'])
        assert fx.exe_success(returncode)
