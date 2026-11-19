from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.dihedral_energies import dihedral_energies


class TestDihedralEnergies():
    def setup_class(self):
        fx.test_setup(self, 'dihedral_energies')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_dihedral_energies(self):
        returncode = dihedral_energies(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.exe_success(returncode)
