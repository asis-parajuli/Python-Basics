from array import array

# referencing https://docs.python.org/3/library/array.html
numbers = array("i", [1, 2, 3])

# we can use append, insert, remove, pop exactly like list
numbers.append(4)
print(numbers)

# we can access items by using their index
# it is interger determined by the type code "i" as an int and if we ad a floating number or any other type we will get an error
# numbers[0] = 1.0
# TypeError: integer argument expected, got float

# using array if we are dealing with large sequence of numbers or encounter a performance problem
# for other cases it is good to use list
