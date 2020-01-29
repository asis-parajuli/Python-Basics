# a collection of key value pairs
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
print(point)

# checking for the existence of the value
if "a" in point:
    print(point["a"])

# if the value doesnot exist bydefault returns none
print(point.get("a"))

# to return any other values except none we can define as below
print(point.get("a", 0))

# to delete an item we use del function
del point["x"]
print(point)

# looping over dictionaries
for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)
