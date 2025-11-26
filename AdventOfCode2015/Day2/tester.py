
from christmas_package_dimensions import ChristmasPackage

christmas_package = ChristmasPackage()

print(christmas_package.read_file('input.txt'))

print(christmas_package.convert_input('13x5x19'))

print(christmas_package.get_summed_area_of_wrapping_paper(christmas_package.read_file('input.txt')))

print(christmas_package.get_smallest_value(10,2,3))

print(christmas_package.calculate_smallest_perimeter(10,5,1))

print(christmas_package.calculate_total_ribbon_length(christmas_package.read_file('input.txt')))
