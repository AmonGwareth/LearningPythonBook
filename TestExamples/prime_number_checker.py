
class PrimeNumberChecker:

    @staticmethod
    def is_prime(number: int):
        """Checks if an Integer prime number.
        Prime numbers are natural numbers, that are greater than 1 that have
        no positive divisors other than 1 and themselves.
        """
        try:
            prime_flag = True
            if number <= 1:
                prime_flag = False
            else:
                for num in range(2, number):
                    if number % num == 0:
                        prime_flag = False

            return prime_flag

        except TypeError as t:
            print(f"Error: {t}")
            print("Please enter a valid Number!")
