

# def my_function(str1, str2):
#     print('This is my function!')
#     print(str1)
#     print(str2)

# my_function('hello', 'world')


# def print_something(name="Jonny", age=50):
#     print('My name is', name, ' and my age is ', age)

# print_something(age=32)



# def print_people(*people):
#     for person in people:
#         print("This person is", person)

# print_people("Jonny", "Leigh", "Charlie")

# def do_math(num1, num2):
#     return num1 + num2

# print(do_math(5, 7))

import re 
# This is Regex
string = '"I AM NOT YELLING", she said.  Thought I know it to be strong'
print(string)
new = re.sub('[A-Z]', '', string)
print(new)
new = re.sub('[^0-9]', '', string)
# This one removes everything apart from numbers



