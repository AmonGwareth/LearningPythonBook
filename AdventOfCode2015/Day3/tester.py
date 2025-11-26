
# my_set = {(1, 2), (1, 1), (1, 1), (0, 0)}
# # my_set.add((1, 3))
#
# my_set = set()
#
# my_set.add((1, 3))
#
# print(my_set)
#
# # with open('input.txt') as file:
# #     input_ = file.readline()
# #
# # print(input_)


# print([1,2] + [2, 2])


# # solution
from House_Counter import HouseCounter
from SplitString import split_data


#
house_counter = HouseCounter()
house_counter.import_input('input.txt')

print(house_counter.data)

# house_counter.deliver_presents()
# print(house_counter.calculate_number_of_delivered_houses())
#
# santa_input = split_data(house_counter.data)[0]
# print(santa_input)
# santa_counter = HouseCounter()
# santa_counter.data = santa_input
# santa_counter.deliver_presents()
#
# robot_santa_input = split_data(house_counter.data)[1]
# print(robot_santa_input)
# robot_santa_counter = HouseCounter()
# robot_santa_counter.data = robot_santa_input
# robot_santa_counter.deliver_presents()
#
# # get the combined lists
# santa_counter.reached_positions.update(robot_santa_counter.reached_positions)
#
# print("Total number of positions reached: ", santa_counter.calculate_number_of_delivered_houses())



