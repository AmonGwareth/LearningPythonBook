class Solution:

    def __init__(self):
        self.current_substring = ""
        self.current_substring_length = 0
        self.longest_substring_length = 0

    def length_of_longest_substring(self, s: str) -> int:

        while s:
            for entry in s[:]:
                if entry not in self.current_substring:
                    self.current_substring += entry
                    self.current_substring_length = len(self.current_substring)
                    continue
                else:
                    if self.current_substring_length > self.longest_substring_length:
                        self.longest_substring_length = self.current_substring_length
                        self.current_substring_length = 0
                        self.current_substring = ""
                    else:
                        self.current_substring_length = 0
                        self.current_substring = ""
                s = s[1:]
                break

        return self.longest_substring_length


