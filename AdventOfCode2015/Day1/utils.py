
def find_the_floor(puzzle: str) -> int:
    current_floor = 0
    for char in puzzle:
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1
    return current_floor


def find_first_basement_entry(puzzle: str) -> (int, str):
    current_floor = 0

    for idx, char in enumerate(puzzle):
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1

        if current_floor < 0:
            print("First basement entry")
            return idx + 1, char


    # return idx, current_floor
