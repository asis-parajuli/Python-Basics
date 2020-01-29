# it shows the index of the charater
letters = ["a", "b", "c", "a"]
print(letters.index("a"))

# what if we type the character that is not present in the list
# this will throw an error
# we should check the presence first as below
if "d" in letters:
    print(letters.index("d"))

# for counting the occurnace of a item in the list we use count
print(letters.count("a"))
