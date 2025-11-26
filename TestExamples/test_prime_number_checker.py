import pytest
from prime_number_checker import PrimeNumberChecker


prime_checker = PrimeNumberChecker()


class TestPrimeNumberChecker:

    @pytest.fixture
    def init_prime_num(self):
        return 7

    @pytest.fixture
    def init_non_prime_num(self):
        return 6

    def test_prime_num(self, init_prime_num):
        assert prime_checker.is_prime(number=init_prime_num)

    def test_non_prime_num(self, init_non_prime_num):
        assert not prime_checker.is_prime(number=init_non_prime_num)

    @pytest.mark.parametrize("prime_num", [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
    def test_prime_list(self, prime_num):
        assert prime_checker.is_prime(number=prime_num)

    @pytest.mark.parametrize("prime_num", [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40])
    def test_non_prime_list(self, prime_num):
        assert not prime_checker.is_prime(number=prime_num)

    def test_string_input(self):
        assert not prime_checker.is_prime(number="String In")

    def test_negative_prime(self):
        assert not prime_checker.is_prime(number=-7)
