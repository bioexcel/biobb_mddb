from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.rmsd_pairwise import rmsd_pairwise


class TestRmsdPairwise():
    def setup_class(self):
        fx.test_setup(self, 'rmsd_pairwise')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_rmsd_pairwise(self):
        returncode = rmsd_pairwise(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_zip_path'])
        assert fx.exe_success(returncode)
