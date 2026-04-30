from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.rmsd_per_residue import rmsd_per_residue


class TestRmsdPerResidue():
    def setup_class(self):
        fx.test_setup(self, 'rmsd_per_residue')

    def teardown_class(self):
        fx.test_teardown(self)
        pass

    def test_rmsd_per_residue(self):
        returncode = rmsd_per_residue(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.equal(self.paths['output_analysis_filepath'], self.paths['ref_output_analysis_filepath'])
        assert fx.exe_success(returncode)
