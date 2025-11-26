import pytest
from House_Counter import HouseCounter
from SplitString import split_data
house_counter = HouseCounter()


class TestDay3:

    @pytest.fixture
    def example_delivery1(self):
        return '^v^v^v^v^v'

    def test_calculate_number_of_delivered_houses(self, example_delivery1):
        house_counter.data = example_delivery1
        house_counter.deliver_presents()
        assert house_counter.calculate_number_of_delivered_houses() == 2

    def test_split_data(self, example_delivery1):
        assert split_data(example_delivery1) == ['^^^^^', 'vvvvv']