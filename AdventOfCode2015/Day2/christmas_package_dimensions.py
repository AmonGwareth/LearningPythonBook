
class ChristmasPackage:

    def get_summed_area_of_wrapping_paper(self, list_):
        total_area = 0
        for entry in list_:
            total_area += self.get_area_of_wrapping_paper(*self.convert_input(entry))
        return total_area

    def get_area_of_wrapping_paper(self, length: float, width: float, height: float) -> float:
        bonus_area = self.get_smallest_value(length*width, width*height, height*length)
        return 2*length*width + 2*width*height + 2*height*length + bonus_area

    @staticmethod
    def get_smallest_value(length: float, width: float, height: float) -> float:
        return min((length, width, height))

    @staticmethod
    def convert_input(input_: str) -> tuple:
        current_string = ''
        list_ = []
        for char in input_:
            if char != 'x':
                current_string += char
            else:
                list_.append(int(current_string))
                current_string = ''
        list_.append(int(current_string))
        return tuple(list_)

    @staticmethod
    def read_file(filename: str) -> list:
        with open(filename) as file:
            list_ = [line.rstrip() for line in file]
        return list_

    @staticmethod
    def calculate_package_volume(length: float, width: float, height: float) -> float:
        return length * width * height

    @staticmethod
    def calculate_smallest_perimeter(length: float, width: float, height: float) -> float:
        list_ = [length, width, height]
        list_.remove(max(list_))
        return list_[0]*2 + list_[1]*2

    def calculate_total_ribbon_length(self, list_) -> float:
        total_ribbon_length = 0
        for entry in list_:
            total_ribbon_length += (self.calculate_smallest_perimeter(*self.convert_input(entry))
                                    + self.calculate_package_volume(*self.convert_input(entry)))

        return total_ribbon_length

