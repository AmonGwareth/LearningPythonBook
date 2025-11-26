import matplotlib.pyplot as plt
import numpy as np
#
# light_array = np.zeros((1000, 1000))
# light_array[226:599, 196:390] = 1
# plt.matshow(light_array)
# plt.show()
# print(light_array)
#
#
#
# print(np.sum(light_array, (0, 1)))
#
#
# entry = 'turn off 660,55 through 986,197'
# entry = 'toggle 322,558 through 977,958'
# # test = entry.split()
# test2 = test[2].split(sep=',')

# print(te)

# import re
#
# splitted = re.split(r'[, \s]', entry)
#
# print(splitted)
#
# row = splitted
# dict_entry = {
#     "action": row[0],
#     "start": (row[1], row[2]),
#     "end": (row[4], row[5]),
# }
#
# test = 1
# print(not test)
#
# print(dict_entry["start"][0])

print(False - 2)


from Light_Array import LightArray
#
# light_array = LightArray()
#
# light_array.read_input_file('input.txt')
# light_array.convert_data()
# light_array.apply_all_instructions()
# print("Number of active lights: ", light_array.number_of_active_lights)
# light_array.visualize_light_array()



# now the brightness

light_array_brightness = LightArray()
light_array_brightness.read_input_file('input.txt')
light_array_brightness.convert_data()
light_array_brightness.apply_all_brightness_instructions()
print("total brightness of active lights: ", light_array_brightness.number_of_active_lights)
light_array_brightness.visualize_light_array()

# instruction = light_array.converted_data[5]

# light_array.toggle_lights(instruction)
# light_array.visualize_light_array()

# light_array.light_array = np.logical_not(light_array.light_array, where=[226:599, 169:390])

# turn on 226,196 through 599,390


# light_array.visualize_light_array()

#
# instruction = light_array.converted_data[10]
#
# light_array.toggle_lights(instruction)
#
# light_array.visualize_light_array()



# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# fig, ax = plt.subplots()
# (line,) = ax.plot(x, y)   # unpack the line object
#
# for i in range(5):
#     y = np.sin(x + i)
#     line.set_ydata(y)     # 🔹 update data
#     plt.pause(0.5)        # 🔹 refresh plot