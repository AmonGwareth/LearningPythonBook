

class ShortestTravelFinder:

    def __init__(self):
        self.data = []
        self.converted_data = []

    def load_data(self, filename: str):
        with open(filename) as file:
            self.data = [line.rstrip() for line in file]

    def convert_data(self):
        for distance in self.data:
            self.converted_data.append()