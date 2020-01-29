# *args
def multiply(*numbers):  # here *numbers indicates there will be multiple arguments as numbers
    total = 1
    for number in numbers:
        # total = total * number
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# **args
def save_user(**user):
    print(user)


save_user(id=1, name="Asis", age=22)
