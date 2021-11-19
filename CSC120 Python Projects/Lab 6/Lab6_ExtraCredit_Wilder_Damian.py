# Given the string,
# s = "i_love_programming_in_python_and_i_will_alzways_program"
# Find all the unique characters in this string. You can use dictionaries or
# two for loops. A unique character is one which appears only once in the
# given string. For example, z or v


s = "i_love_programming_in_python_and_i_will_alzways_program"

already_found = []

for char in s:
    if char not in already_found:
        already_found.append(char)
for unique in already_found:
    print(f'Unique character: {unique}')
