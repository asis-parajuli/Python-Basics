# for the purpose of sorting the number in order we use sort()
numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers)

# for the purpose of sorting the number in descenting order we use parameter reverse=True
numbers.sort(reverse=True)
print(numbers)

# within the sort function we have a built in function sorted()
print(sorted(numbers))

# we can add arguement in the sorted function like as
print(sorted(numbers, reverse=True))

# what if we have a list of tuples
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product1", 12)
]

# we need to define a funtion to sort this type of list

# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

# the above commented function can be cleaned by using Lambda Functions
items.sort(key=lambda item: item[1])
print(items)


# Map function
# what if we are only interseted in the price of the product and want to transfer price into a new list

# prices = []
# for item in items:
#     prices.append(item[1])

# instead of the above loop we can use map function
prices = list(map(lambda item: item[1], items))
# map function returns map object which is another iterable
print(prices)


# filter functions
# we want to filter the list as whose price is equal or greater than 10
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)


# List Comprehensions
# it produces the same result of what we have in line 45
prices = [item[1] for item in items]  # replacing map function
print(prices)

# it produces the same result of what we have in line 52
# replacing filter function
filtered = [item for item in items if item[1] >= 10]
print(filtered)


# Zip function
list1 = [1, 2, 3]
list2 = [10, 20, 30]

# what if we want to have this result [(1,10) , (2,20), (3,30)]
# we are combining two list for this we use built in zip function
print(list(zip(list1, list2)))  # it returns a zip object which is iterable

# what if we want this result [("a", 1, 10), ("b", 2, 20),("c", 3, 30))]
print(list(zip("abc", list1, list2)))  # we simply add a string "abc"
