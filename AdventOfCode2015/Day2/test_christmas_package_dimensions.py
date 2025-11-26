
import pytest
from christmas_package_dimensions import ChristmasPackage

christmas_package = ChristmasPackage()


class TestChristmasPackage:

    @pytest.fixture
    def example_package_dimensions(self):
        return 2, 3, 4

    @pytest.fixture
    def example_package_dimensions2(self):
        return 1, 1, 10

    # @pytest.fixture
    # def example_package_dimensions2(self):
    #     return 1, 1, 10

    # test get area
    def test_example_package(self, example_package_dimensions):
        assert christmas_package.get_area_of_wrapping_paper(*example_package_dimensions) == 58

    def test_example_package2(self, example_package_dimensions2):
        assert christmas_package.get_area_of_wrapping_paper(*example_package_dimensions2) == 43

    # tests for smallest
    def test_smallest_dimension(self, example_package_dimensions):
        assert christmas_package.get_smallest_value(*example_package_dimensions) == 2

    def test_smallest_dimension2(self, example_package_dimensions2):
        assert christmas_package.get_smallest_value(*example_package_dimensions2) == 1
