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

# data = ("John", "Doe", 53.44)
# format_string = "Hello %s %s. Your current balance is $%s."

# You can also use f strings.  print(f"hello {variable}")

# print(format_string % data)

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)

# Useful String Methods

# astring = "Hello world!"
# print(astring.index("o"))
# print(astring.count("l"))
# print(astring[3:7])
# print(astring[::-1])
# print(astring.upper())
# print(astring.lower())
# print(astring.startswith("Hello"))
# print(astring.endswith("asdfasdfasdf"))
# print(astring.split(" "))

# For and WHile loop example

# Prints out 0,1,2,3,4

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x)

# Classes etc

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# Code
car1 = Vehicle()
car2 = Vehicle()
car1.color = "red"
car1.value = 60000.00
car1.name = "fer"
car2.color = "blue"
car2.value = 10000.00
car2.name = "Jump"
car2.kind = "van"
# test code
print(car1.description())
print(car2.description())