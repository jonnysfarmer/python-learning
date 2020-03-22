# # THe Basics

# one = 1
# two = float(2)
# three = one + two
# print(three)

# hello = "hello"
# world = "world"
# helloworld = hello + " " + world
# print(helloworld)

# # You can also assign multiple variables
# a, b = 3, 4
# print(a,b)

# Lists

# numbers = []
# numbers.append(1)
# print(numbers)

# Inputting data into strings

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)