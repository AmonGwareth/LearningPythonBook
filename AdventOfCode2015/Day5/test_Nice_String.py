import pytest
from Nice_String import NiceString


class TestNiceString:

    @pytest.fixture
    def counter_string(self):
        return 'aeiouaeiouaeiou'

    @pytest.fixture
    def double_letter_string(self):
        return 'abcdde'

    @pytest.fixture
    def double_letter_string2(self):
        return 'jchzalrnumimnmhp'

    @pytest.mark.parametrize("input_string", ['ugknbfddgicrmopn', 'aaa'])
    def test_nice_strings(self, input_string):
        nice_string = NiceString()
        nice_string.data = input_string
        nice_string.run_string_analysis()
        assert nice_string.is_nice()

    @pytest.mark.parametrize("input_string", ['jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb'])
    def test_naughty_strings(self, input_string):
        nice_string = NiceString()
        nice_string.data = input_string
        nice_string.run_string_analysis()
        assert not nice_string.is_nice()

    def test_vowel_counter(self, counter_string):
        nice_string = NiceString()
        nice_string.data = counter_string
        nice_string.check_num_of_vowels()
        assert nice_string.num_of_vowels == len(counter_string)

    def test_double_letters(self, double_letter_string):
        nice_string = NiceString()
        nice_string.data = double_letter_string
        nice_string.check_for_double_letters()
        assert nice_string.has_double_letter

    def test_double_letters2(self, double_letter_string2):
        nice_string = NiceString()
        nice_string.data = double_letter_string2
        nice_string.check_for_double_letters()
        assert not nice_string.has_double_letter
