from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.distance_per_residue import distance_per_residue


class TestDistancePerResidue():
    def setup_class(self):
        fx.test_setup(self, 'distance_per_residue')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_distance_per_residue(self):
        returncode = distance_per_residue(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_zip_path'])
        assert fx.exe_success(returncode)
