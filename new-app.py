# conditional statement
temperature = 15
if temperature > 30:
    print("It's warm")
    print("drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

# Ternary Operator
age = 12
message = "Eligable" if age >= 18 else "Not Eligable"
print(message)

# Logical Operator
high_income = True
good_credit = False
student = True

# and operator
if high_income and good_credit:
    print("Eligable")
else:
    print("Not Eligable")

# or operator
if high_income or good_credit:
    print("Eligable")
else:
    print("Not Eligable")


# not operator
if not student:
    print("Eligable")
else:
    print("Not Eligable")

# Chaining Comparision Operators
age = 22
if 18 <= age < 65:
    print("Eligible")

# For loop
for number in range(1, 10, 2):  # number is a variable of type integer
    print("Attempt", number, number * ".")

# For else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times but failed.")


# Nested Loops
for x in range(5):  # outer loop
    for y in range(3):  # inner loop
        print(f"({x},{y})")

# Iterables
print(type(5))
print(type(range(5)))

for x in "Python":
    print(x)
for y in [1, 2, 3, 4]:
    print(y)


# While Loops
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)


# infinite loops
# loop that runs forever
