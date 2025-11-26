

class NiceString:

    def __init__(self):
        self.data = ''
        self.num_of_vowels = 0
        self.has_double_letter = False
        self.includes_naughty_strings = False
        self.data_list = []
        self.is_nice_counter = 0
        self.has_nice_repetition = False
        self.contains_pair_of_two_letters = False

    def is_nice(self):
        return self.num_of_vowels >= 3 and self.has_double_letter and not self.includes_naughty_strings

    def check_num_of_vowels(self):
        self.num_of_vowels = sum(1 for char in self.data if char in 'aeiou')

    def check_for_naughty_strings(self):
        for naughty in ['xy', 'ab', 'cd', 'pq']:
            if naughty in self.data:
                self.includes_naughty_strings = True

    def check_for_double_letters(self):
        last_char = ''
        for char in self.data:
            if last_char == char:
                self.has_double_letter = True
            last_char = char

    def run_string_analysis(self):
        self.check_num_of_vowels()
        self.check_for_double_letters()
        self.check_for_naughty_strings()
        # print(
        #     "Analysis results in:", f"num of vowels: {self.num_of_vowels}\n",
        #     f"has_double_letter: {self.has_double_letter}\n", f"includes_naughty_strings: {self.includes_naughty_strings}\n"
        # )

    def read_input(self, filename):
        with open(filename) as file:
            self.data_list = [line.rstrip() for line in file]

    def analyze_data_list(self):
        for data in self.data_list:
            self.data = data
            # restore defaults! not so nice but for now we do it here
            self.has_double_letter = False
            self.num_of_vowels = 0
            self.includes_naughty_strings = False
            #analysis
            self.run_string_analysis()

            if self.is_nice():
                self.is_nice_counter += 1

    def new_rule_char_repeats_after_one_letter(self):
        second_last_char = self.data[0]
        for idx, letter in enumerate(self.data):

            if idx >= 2:
                # print(idx, letter, second_last_char)
                if letter == second_last_char:
                    self.has_nice_repetition = True
                second_last_char = self.data[idx-1]

    def new_rule_contain_any_pair_of_two_letters(self):
        new_list = []
        for idx, char in enumerate(self.data):
            if idx < len(self.data) - 1:
                new_list.append(self.data[idx] + self.data[idx + 1])


        # filter direct repetition
        last_double_char = ''
        for double_char in new_list:
            # removes repetition like aaa
            if last_double_char == double_char:
                new_list.remove(double_char)
            last_double_char = double_char

        if len(new_list) != len(set(new_list)):
            self.contains_pair_of_two_letters = True
        # print(new_list, len(new_list))
        # print(set(new_list), len(set(new_list)))

    def run_string_analysis_rule_set_2(self):
        self.new_rule_char_repeats_after_one_letter()
        self.new_rule_contain_any_pair_of_two_letters()

    def is_nice_ruleset2(self):
        return self.contains_pair_of_two_letters and self.has_nice_repetition

    def analyze_data_list_rule_set_2(self):
        for data in self.data_list:
            self.data = data
            # restore defaults! not so nice but for now we do it here
            self.contains_pair_of_two_letters = False
            self.has_nice_repetition = False
            # analysis
            self.run_string_analysis_rule_set_2()
            if self.is_nice_ruleset2():
                self.is_nice_counter += 1


