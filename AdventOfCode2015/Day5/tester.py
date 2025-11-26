
# print(3 >= 3 and True and not False)

# print(0 + idx for idx, char in enumerate('aeiouaeiouaeiou') if char in 'aeiou')


# print('a' in 'aeiou')
#
# print(len(set('jchzalrnumimnmhp')))
#
# print(len(set('jchzalrnumimnmhp')) == len('jchzalrnumimnmhp'))
#
# if not None:
#     print("test")

from Nice_String import NiceString

# string_checker = NiceString()
#
# # string_checker.data = 'jchzalrnumimnmhp'
# # string_checker.data = 'dvszwmarrgswjxmb'
# # string_checker.data = 'haegwjzuvuyypxyu'
#
# string_checker.data = 'aaa'
# # string_checker.data = 'aaa'
#
# string_checker.run_string_analysis()
# print(string_checker.is_nice())
#
# # string_checker.check_for_double_letters()
#
# # print(string_checker.has_double_letter)


# # ex1
# string_checker.read_input('input.txt')
# string_checker.analyze_data_list()
# # print(string_checker.data_list)
#
#
# print(string_checker.is_nice_counter)

# ex2

# string_checker.data = 'abcdefeghi'
#
# string_checker.new_rule_char_repeats_after_one_letter()
# print(string_checker.has_nice_repetition)
#
#
# # test_data = 'aabcdefgaa'
# test_data = 'abcdefghi'

# new_list = []
# for idx, char in enumerate(test_data):
#     if idx < len(test_data) - 1:
#         new_list.append(test_data[idx] + test_data[idx + 1])
#
# print(new_list, len(new_list))
# print(set(new_list), len(set(new_list)))

string_checker = NiceString()

string_checker.read_input('input.txt')
print(string_checker.data_list)
print(len(string_checker.data_list))
string_checker.analyze_data_list_rule_set_2()
# print(string_checker.data_list)

print(string_checker.is_nice_counter)

# string_checker2 = NiceString()

# string_checker2.data = 'qjhvhtzxzqqjkmpb'
# string_checker2.data = 'xxyxx'
# string_checker2.data = 'uurcxstgmygtbstg'
# string_checker2.data = 'ieodomkazucvgmuy'
# string_checker2.data = 'aaa'
# string_checker2.run_string_analysis_rule_set_2()


# print(string_checker2.is_nice_ruleset2())

