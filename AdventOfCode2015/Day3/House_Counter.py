import numpy as np


class HouseCounter:

    def __init__(self):
        self.data = ''
        self.current_position = (0, 0)
        self.reached_positions = set()

    def import_input(self, file_path: str):
        with open(file_path) as file:
            self.data = file.readline()

    def update_position(self, direction: tuple):
        self.current_position = tuple(np.add(self.current_position, direction))

    @staticmethod
    def convert_symbol_to_direction(symbol: str) -> tuple:
        if symbol == '^':
            return 0, 1
        elif symbol == '<':
            return -1, 0
        elif symbol == '>':
            return 1, 0
        elif symbol == 'v':
            return 0, -1
        else:
            return 0, 0

    def deliver_presents(self):
        self.reached_positions.add(self.current_position)
        for symbol in self.data:
            self.update_position((self.convert_symbol_to_direction(symbol)))
            self.reached_positions.add(self.current_position)

    def calculate_number_of_delivered_houses(self):
        return len(self.reached_positions)

