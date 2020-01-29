# tuples are emutable means we can't modify them
point = (1, 2)
# in tuple we can ignore parenthenisis like point = 1 , 2
# if we have only one item in tuple we should use tralying comma like point = 1,
# for defining an empty tuple we should use empty parenthesis like point = ()

# we can concatinate one tuple with another
point = (1, 2) + (3, 4)
print(point)

# we can use a repetation operator to repeat a tuple
point = (1, 2) * 3
print(point)

# we can convert a list into tuple
point = tuple([1, 2])
print(point)
# strings
point = tuple("hello world")
print(point)

# we can access individual item in a tuple by using an index
point = (1, 2, 3)
print(point[0])
print(point[0:2])

# we can unpack the tuple
x, y, z = point
if 10 in point:
    print("exists")
else:
    print("doesn't exists")

# tuple in real world is used to prevent accidental modification of a sequence or order
