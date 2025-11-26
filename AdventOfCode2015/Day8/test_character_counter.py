import pytest
from character_counter import CharacterCounter

character_counter = CharacterCounter()

class TestCharacterCounter:

    @pytest.fixture
    def test_data(self):
        return ["", "abc", "aaa\"aaa", "\x27"]

    def test_character_counter(self, test_data):
        character_counter.data = test_data
        character_counter.count_num_of_chars_string()
        character_counter.count_num_of_chars_code()
        assert (character_counter.num_of_chars_code - character_counter.num_of_chars_string) == 12
