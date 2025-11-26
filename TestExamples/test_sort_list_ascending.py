import pytest
from utils import list_is_sorted_ascending


class TestAscendingListCreator:

    @pytest.fixture
    def simple_ascending_list(self):
        return list(range(20))

    @pytest.fixture
    def simple_descending_list(self):
        return list(range(20))[::-1]

    @pytest.fixture
    def empty_list(self):
        return []

    @pytest.fixture
    def truecase1(self):
        return [1, 1, 1, 1, 2]

    @pytest.fixture
    def falsecase1(self):
        return [10, 15, 7, 9]

    @pytest.fixture
    def string_list(self):
        return ["nice", "to", "meet", "you"]

    @pytest.fixture
    def string_list2(self):
        return ["nice", "nice", "nice", "nice"]

    def test_simple_ascending_list(self, simple_ascending_list):
        assert list_is_sorted_ascending(simple_ascending_list)

    def test_simple_descending_list(self, simple_descending_list):
        assert not list_is_sorted_ascending(simple_descending_list)

    def test_turecase1(self, truecase1):
        assert list_is_sorted_ascending(truecase1)

    def test_falsecase1(self, falsecase1):
        assert not list_is_sorted_ascending(falsecase1)

    def test_empty_list(self, empty_list):
        assert not list_is_sorted_ascending(empty_list)  # empty list is not ascending

    def test_string_list(self, string_list):
        assert not list_is_sorted_ascending(string_list)

    def test_string_list2(self, string_list2):
        assert not list_is_sorted_ascending(string_list2)

