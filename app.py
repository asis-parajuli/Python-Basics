# print("Hello world")
# print("*" * 10)

# Working With Numbers
import math
print(round(2.9))  # rounding of a number
print(abs(-2.9))  # absolute value of a number which results positive 2.9
# importing math library
print(math.ceil(2.2))
# list from math library
# https://docs.python.org/3/library/math.html

# variables
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
# len function is used to count the total number of character in the string
print(len(course_name))
print(course_name[0])
# Negative index (-1) returns to the last character of the string
print(course_name[-1])
# slicing a string. A character at the end which is 3 is not included
print(course_name[0:3])
# without the last index which is missing below 0: this is return exact same of the orginal string
print(course_name[0:])
print(course_name[:3])
print(course_name[:])


# Escape Sequence
# \ backslash is used to escape the character after it
# \ backslash \" , \\ , \' are escape sequences
# \n is for new line
course = "Python \nProgramming"
print(course)

# Formatted string
first = "Aashish"
last = "Parajuli"
full = f"{first} {last}"
# when we are using formatted string we can use any valid expression inbetween curly braces {}
# full = f"{first(first)} {last}"
print(full)

# String Methods
new_course = "  python Programming"
print(new_course.upper())
print(new_course.lower())
# title() is used to capital initial letter of the word
print(new_course.title())
# stip() is used to remove añny white space at the begning or at the end
# lstrip() is for left strip and rstrip() is for right strip
print(new_course.strip())
# to find the index we use find()
print(new_course.find("m"))
# we can use multiple character using find()
print(new_course.find("ing"))
# to replace a character we use replace() we replace all p with k
print(new_course.replace("p", "k"))
# to check the existance of a character we use "in"
print("Pro" in new_course)
# find() return an index while "in" returns a boolean
# "not in" is used to check the absence of character in a string
print("ramean" in new_course)


# Numbers
x = 1  # integer
x = 1.1  # float
x = 2 + 1j  # complex number # a + bi where i is an imaginary number
print(10 + 3)  # addition
print(10 - 3)  # substraction
print(10 * 3)  # multiplicatio
print(10 / 3)  # division
print(10 // 3)  # division which provides result as integer
print(10 % 3)  # modulous result will be a remainder
print(10 ** 3)  # exponential means 10 to the power 3
# augmented assignment operator
x = 10
x += 3  # augmented assignment operator which provides the same result as x = x + 3

# Type Conversion
x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")
# conversion type
# int(x)
# float(x)
# bool(x)
# str(x)

# Falsy value => "", 0 , none
# All other will be True
