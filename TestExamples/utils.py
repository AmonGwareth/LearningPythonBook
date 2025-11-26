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


def list_is_sorted_ascending(list_: list[int | float]):
    """Checks if a list is sorted in ascending order."""

    try:
        if not all(isinstance(x, (int, float)) for x in list_):
            raise TypeError("list_ must contain only numbers!")

        is_ascending = True

        if not list_:
            is_ascending = False
        else:
            last_entry = list_[0]

            for idx, entry in enumerate(list_):
                if idx > 1:
                    if last_entry <= entry:
                        last_entry = entry
                    else:
                        is_ascending = False
            return is_ascending

    except TypeError:
        print("Please Check the Input --> only ints or floats")





