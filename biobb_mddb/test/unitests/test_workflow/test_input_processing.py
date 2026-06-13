from biobb_common.tools import test_fixtures as fx
from biobb_mddb.workflow.input_processing import input_processing


class TestInputProcessing():
    def setup_class(self):
        fx.test_setup(self, 'input_processing')

    def teardown_class(self):
        fx.test_teardown(self)

    def test_input_processing(self):
        returncode = input_processing(properties=self.properties, **self.paths)
        assert fx.not_empty(self.paths['output_topology_filepath'])
        assert fx.equal(self.paths['output_topology_filepath'], self.paths['ref_output_topology_filepath'])
        assert fx.not_empty(self.paths['output_trajectory_filepath'])
        assert fx.equal(self.paths['output_trajectory_filepath'], self.paths['output_trajectory_filepath'])
        assert fx.not_empty(self.paths['output_structure_filepath'])
        assert fx.equal(self.paths['output_structure_filepath'], self.paths['output_structure_filepath'])
        assert fx.exe_success(returncode)
