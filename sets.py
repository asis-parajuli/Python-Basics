# set is the collection of only unique values
numbers = [1, 1, 2, 3, 4]
first = set(numbers)

# curley braces is used to define sets {}
second = {1, 5}
# basic functions like append remove add pop are supported in sets

# vertical bar '|' represents union
print(first | second)
print(first & second)  # intersection is defined by & symbol
print(first - second)  # difference of two set is defined by '-' minus symbol
print(first ^ second)  # all items except common items

# set object doesnot support indexing

# we can check if the item is in the set or not
if 1 in first:
    print("yes")
