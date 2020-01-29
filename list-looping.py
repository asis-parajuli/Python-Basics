# looping over lists
letters = ["a", "b", "c"]
# for the purpose of getting index of the item of the list we use enumerate
for index, letter in enumerate(letters):
    print(index, letter)


# Adding and removing items from list
# for adding item we have 2 options
letters.append("d")  # append is for adding at the last
print(letters)

# insert to add to a particular positin using index
letters.insert(0, "-")
print(letters)

# for removing we have different options
letters.pop()  # pop is used to remove the last item of the list
print(letters)

# we use pop() with index for removing a particular item form a list
letters.pop(0)  # here pop(0) indicates removing the item form the index 0
print(letters)

# we can use remove() to remove the particular item form the list
# this will remove the first occurance of "b" from the list
letters.remove("b")
print(letters)

# another way of deleting is by using del
del letters[0]
# we can also remove a range of items by using del letters[0:3]


# with pop() we can remove a item at a time but with del we can remove a range of items

# if we want to delete all items from the list then we should use letters.clear()
letters.clear()
