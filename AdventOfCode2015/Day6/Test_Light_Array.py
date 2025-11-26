import pytest
from Light_Array import LightArray
import numpy as np

my_light_array = LightArray()


class TestLightArray:

    @pytest.fixture
    def instruction_all_on(self):
        return {"action": 'turn on', "start": (0, 0), "end": (999, 999)}

    def test_all_lights_on(self, instruction_all_on):
        my_light_array.toggle_lights(instruction_all_on)
        print("number of active lights:", np.sum(my_light_array.light_array))
        assert np.sum(my_light_array.light_array, axis=(0, 1)) == 1000*1000
