import pytest
from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.chemical_shifts import chemical_shifts


@pytest.mark.skip(reason='Stand by: LEGOLAS is not fully integrated in the MDDB workflow yet')
class TestChemicalShifts():
    def setup_class(self):
        fx.test_setup(self, 'chemical_shifts')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_chemical_shifts(self):
        returncode = chemical_shifts(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.equal(self.paths['output_analysis_filepath'], self.paths['ref_output_analysis_filepath'])
        assert fx.exe_success(returncode)
