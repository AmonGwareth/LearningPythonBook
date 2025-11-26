import pytest
from santas_bitwise_logic_gate import BitwiseLogicGate

santas_gate = BitwiseLogicGate()


class TestBitwiseLogicGate:

    @pytest.fixture
    def first_lshift_instruction(self):
        return {'type': 'connection', 'operator': 'LSHIFT', 'in_val': 'c', 'in_val2': '1', 'out_val': 't'}

    # @pytest.fixture



    def test_lshift_instruction(self, first_lshift_instruction):
        santas_gate.variables.append({'name': 'c', 'val': '0'})
        santas_gate.converted_data = [first_lshift_instruction]
        santas_gate.update_instruction_list()
        assert santas_gate.converted_data == [{'type': 'connection', 'operator': 'LSHIFT', 'in_val': '0', 'in_val2': '1', 'out_val': 't'}]