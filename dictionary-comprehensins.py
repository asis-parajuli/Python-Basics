values = {}
for x in range(5):
    values[x] = x * 2

# the above expression can be replaced by a single line of code shown below
values = {x: x*2 for x in range(5)}
print(values)
