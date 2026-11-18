from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.membrane_channels import membrane_channels


class TestMembraneChannels():
    def setup_class(self):
        fx.test_setup(self, 'membrane_channels')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_membrane_channels(self):
        returncode = membrane_channels(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_analysis_filepath'])
        assert fx.exe_success(returncode)
