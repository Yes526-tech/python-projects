starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
#-----------------------------------------------------------------------------------------------------
# print(final_dictionary = starting_dictionary.append(["c": 7]))

#  File "C:/Users/ysert/PycharmProjects/pythonProject/test_quiz/testing.py", line 12
#     print(final_dictionary = starting_dictionary.append(["c": 7]))
#                                                             ^
# SyntaxError: invalid syntax
# Process finished with exit code 1
#-----------------------------------------------------------------------------------------------------
# print(final_dictionary = starting_dictionary += {"c" = 7})

#   File "C:/Users/ysert/PycharmProjects/pythonProject/test_quiz/testing.py", line 13
#     print(final_dictionary = starting_dictionary += {"c" = 7})
#                                                  ^
# SyntaxError: invalid syntax
#-----------------------------------------------------------------------------------------------------
# print(final_dictionary = starting_dictionary["c"] : 7)

#   File "C:/Users/ysert/PycharmProjects/pythonProject/test_quiz/testing.py", line 24
#     print(final_dictionary = starting_dictionary["c"] : 7)
#                                                       ^
# SyntaxError: invalid syntax
#
# Process finished with exit code 1
#-----------------------------------------------------------------------------------------------------
# print(final_dictionary = starting_dictionary["c"] = 7)

#   File "C:/Users/ysert/PycharmProjects/pythonProject/test_quiz/testing.py", line 24
#     print(final_dictionary = starting_dictionary["c"] : 7)
#                                                       ^
# SyntaxError: invalid syntax
#
# Process finished with exit code 1
#-----------------------------------------------------------------------------------------------------

starting_dictionary["c"] = 7
starting_dictionary = final_dictionary
print(starting_dictionary)