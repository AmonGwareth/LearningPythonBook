import re
import numpy as np
import matplotlib.pyplot as plt
import time
# import seaborn as sns


class LightArray:

    def __init__(self):
        self.data = []
        self.converted_data = []
        self.light_array = np.zeros((1000, 1000), dtype=bool)
        self.number_of_active_lights = 0

    def read_input_file(self, filename: str):
        """Just reads the txt file line by line."""
        with open(filename) as file:
            self.data = file.readlines()

    def convert_data(self):
        """Converts the initial input data into a list of instructions as dictionary."""
        for entry in self.data:
            row = re.split(pattern=r'[, \s]', string=entry)
            if len(row) == 7:
                dict_entry = {
                    "action": row[0],
                    "start": (int(row[1]), int(row[2])),
                    "end": (int(row[4]), int(row[5])),
                }
            elif len(row) == 8:
                dict_entry = {
                    "action": row[0] + ' ' + row[1],
                    "start": (int(row[2]), int(row[3])),
                    "end": (int(row[5]), int(row[6])),
                }
            else:
                dict_entry = None

            self.converted_data.append(dict_entry)

    def toggle_lights(self, instruction: dict):
        """ Apply the instruction dictionary to the current light array."""
        if instruction["action"] == 'turn on':
            self.light_array[
                instruction["start"][0]:instruction["end"][0]+1, instruction["start"][1]:instruction["end"][1]+1
            ] = True
        elif instruction["action"] == 'turn off':
            self.light_array[
                instruction["start"][0]:instruction["end"][0]+1, instruction["start"][1]:instruction["end"][1]+1
            ] = False
        elif instruction["action"] == 'toggle':
            self.light_array[
                instruction["start"][0]:instruction["end"][0]+1, instruction["start"][1]:instruction["end"][1]+1
            ] = np.logical_not(self.light_array[
                instruction["start"][0]:instruction["end"][0]+1, instruction["start"][1]:instruction["end"][1]+1
            ])

    def visualize_light_array(self):
        """Creates simple plot of the current light array."""
        plt.matshow(self.light_array, cmap='viridis')
        plt.title('Santa´s Light Array')
        plt.show()

    def apply_all_instructions(self):
        """Apply all instructions to the light array."""
        for instruction in self.converted_data:
            self.toggle_lights(instruction)
            self.number_of_active_lights = np.sum(self.light_array, axis=(0, 1))  # useful for intermediate results
            # self.visualize_light_array()

    def change_brightness(self, instruction: dict):
        """Apply all instructions but with the new rule set.
        turn on: increase brightness by 1
        turn off: reduce brightness by 1 - minimum zero!
        toggle: increase brightness by 2
        """
        if instruction["action"] == 'turn on':
            self.light_array[
                instruction["start"][0]:instruction["end"][0]+1, instruction["start"][1]:instruction["end"][1]+1
            ] += 1
        elif instruction["action"] == 'turn off':
            self.light_array[
                instruction["start"][0]:instruction["end"][0]+1, instruction["start"][1]:instruction["end"][1]+1
            ] -= 1
            self.light_array[self.light_array < 0] = 0
        elif instruction["action"] == 'toggle':
            self.light_array[
                instruction["start"][0]:instruction["end"][0]+1, instruction["start"][1]:instruction["end"][1]+1
            ] += 2

    def apply_all_brightness_instructions(self):
        """Apply all instructions to the light array."""

        self.light_array = np.zeros((1000, 1000), dtype=int)

        for instruction in self.converted_data:
            self.change_brightness(instruction)
            self.number_of_active_lights = np.sum(self.light_array, axis=(0, 1))  # useful for intermediate results
            # self.visualize_light_array()
