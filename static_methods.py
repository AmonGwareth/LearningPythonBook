
class StringUtilOld:
    @staticmethod
    def is_palindrome(s, case_insensitive=True):
        # we allow only letters and numbers
        s = "".join(c for c in s if c.isalnum()) # only uses alphanumeric characters (a-z) and (0-9)
        # For case insensitve comparision, change to lower cases
        if case_insensitive:
            s = s.lower()
        for c in range(len(s)//2):
            if s[c] != s[-c-1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


class StringUtil:
    @classmethod
    def is_palindrome(cls, s, case_insensitive=True):
        # we allow only letters and numbers
        s = cls._strip_string(s)
        # For case-insensitive comparison, change to lower cases
        if case_insensitive:
            s = s.lower()
        return cls._is_palindrome(s)

    @staticmethod
    def _strip_string(s):
        return "".join(c for c in s if c.isalnum()) # only uses alphanumeric characters (a-z) and (0-9)

    @staticmethod
    def _is_palindrome(s):
        for c in range(len(s)//2):
            if s[c] != s[-c-1]:
                return False
        return True

    @staticmethod
    def get_unique_words(sentence):
        return set(sentence.split())


