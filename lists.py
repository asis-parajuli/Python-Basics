letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 100  # 100 zeros
print(zeros)

combined = zeros + letters
print(combined)

# list of numbers
numbers = list(range(20))
print(numbers)

# list of strings
chars = list("Hello World")
print(chars)

# to print the length of the list
print(len(chars))


# Accessing Items
letters = ["a", "b", "c", "d"]
print(letters[0])
# modifying items in list
letters[0] = "A"
print(letters)

# slicing a list
print(letters[0:3])
print(letters[:3])  # it is same as above line

# passing a step during slicing by using ::
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])  # this will return every other element in the list

# this will return the original list but in the reverse order
print(numbers[::-1])


# Unpacking a list
numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# above 3 commented lines provides the same output of the line below
first, second, third = numbers  # list unpacking

# what if we have a list with large number of items but we care for only first 2
numbers = [1, 2, 3, 4, 5, 6, 8, 1, 4, 2]
# we pack the rest into seperate list
first, second, *other = numbers
print(first)
print(other)

# what if we only care about first and last item
numbers = [1, 2, 3, 4, 5, 6, 8, 1, 4, 2]
first, *other, last = numbers
print(first, last)
print(other)
