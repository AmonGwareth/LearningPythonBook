from codecs import decode

class CharacterCounter:

    def __init__(self):
        self.data = []
        self.num_of_chars_string = 0
        self.num_of_chars_code = 0

    def load_input_file(self, filename: str):
        with open(filename) as file:
            self.data = [line.rstrip()[1:-1] for line in file]

    def load_input_file_include_surrounding(self, filename: str):
        with open(filename) as file:
            self.data = [line.rstrip() for line in file]

    def count_num_of_chars_string(self):
        for string in self.data:
            # print(string, len(string))
            self.num_of_chars_string += len(decode(string, "unicode_escape"))

    def count_num_of_chars_code(self):
        for string in self.data:
            string = r"{}".format(string)
            # print(string, len(string)+2)
            self.num_of_chars_code += (len(string)+2)


