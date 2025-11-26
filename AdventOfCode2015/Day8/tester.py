
# # test_string = r'v\xfb\"lgs\"kvjfywmut\x9cr'
# # test_string2 = 'v\xfb\"lgs\"kvjfywmut\x9cr'
# #
# # # test_string = r'"\x27"'
# # # test_string2 = '"\x27"'
# # #
# # # test_string = test_string.strip('""')
# # # test_string2 = test_string2.strip('""')
# # # # #
# # test_string = r'azlgxdbljwygyttzkfwuxv'
# # test_string2 = 'azlgxdbljwygyttzkfwuxv'
# # #
# #
# # "kyogyogcknbzv\x9f\\\\e"
# #
# #
# # test_string = r"kyogyogcknbzv\x9f\\\\e"
# # test_string2 = "kyogyogcknbzv\x9f\\\\e"
# #
# # # test_string = r""
# # # test_string2 = ""
# #
# # # test_string = r"abc"
# # # test_string2 = "abc"
# #
# test_string = r"aaa\"aaa"
# test_string2 = "aaa\"aaa"
# #
# # test_string = r'aaa\"aaa'
# # test_string2 = 'aaa\"aaa'
# # #
# # test_string = r'\x27'
# # test_string2 = '\x27'
#
# # print("\x27")
# #
# #
# #
# # #
# print(test_string, len(test_string) + 2)
# print(test_string2, len(test_string2))
#
# test_string = r'mxvlz\\"fwuvx\\"cyk\\'
# test_string2 = 'mxvlz\\"fwuvx\\"cyk\\'


from character_counter import CharacterCounter
#
my_counter = CharacterCounter()
#
# my_counter.load_input_file('input.txt')
my_counter.load_input_file_include_surrounding('test_input.txt')
my_counter.count_num_of_chars_string()
my_counter.count_num_of_chars_code()



# print(my_counter.data)
#
print(my_counter.num_of_chars_code - my_counter.num_of_chars_string)
#
# from codecs import decode
#
# print(decode(my_counter.data[2], encoding='unicode_escape'))


import codecs

print(codecs.ascii_encode('""'))
