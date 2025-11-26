from santas_bitwise_logic_gate import BitwiseLogicGate
# import re

santas_logic_gate = BitwiseLogicGate()

santas_logic_gate.read_input_file('input2.txt')
#
santas_logic_gate.convert_data()
#
# print(santas_logic_gate.assignment_data)
# print(santas_logic_gate.connection_data)
# print(santas_logic_gate.NOT_data)
print(santas_logic_gate.unhandled_data)
print(santas_logic_gate.converted_data)

#
#
#
santas_logic_gate.build_logic_gate()
print(santas_logic_gate.variables)
print(santas_logic_gate.converted_data)
#
# santas_logic_gate.variables.append({'name': 'c', 'val': '0'})
# santas_logic_gate.converted_data = [{'type': 'connection', 'operator': 'LSHIFT', 'in_val': 'c', 'in_val2': '1', 'out_val': 't'}]
# santas_logic_gate.update_instruction_list()
#
# print(santas_logic_gate.converted_data)

# my_set = {{'name': 'test'}, {'name': 'test'}}
#
# print(my_set)

# print(bin(5))
# print(bin(3))
# print(5 | 3)
# print(bin(5 or 3))
# print(bin(5) | bin(3))
# print(santas_logic_gate.data[2].split())
#
# print(len(['x', 'AND', 'y', '->', 'd']))

# print((a = 1, b = 2, c = 3))

# my_dict = {
#     "type": 'connection',
#     "operator": "AND",
#     "input_1": 'x',
#     "input_2": 'y',
#     "output": 'd',
# }
#
# my_dict2 = {
#     "type": 'input',
#     "name": 'z',
#     "initial_val": 123,
#     "current_val": 123,
# }
#
# my_dict3 = {
#     "type": 'input',
#     "name": 'y',
#     "initial_val": 456,
#     "current_val": 456,
# }
#
# list_ = [my_dict, my_dict2, my_dict3]
# # list_ = [my_dict2, my_dict3]
#
# print([d for d in list_ if 'name' in d and d['name'] == 'x'])
#
# # for d in list_:
# #     print(d['name'])
# #     # if d['name'] == 'x':
# #         # print("found")