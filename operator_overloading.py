class Weird:
    def __init__(self, s):
        self._s = s

    def __len__(self):
        return len(self._s)

    def __bool__(self):
        return "42" in self._s

    def __add__(self, s2):
        return Weird("Combined String: " + self._s + " " + s2._s)

