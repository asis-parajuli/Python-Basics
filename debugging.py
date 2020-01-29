def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
        # return total  # return should be intendent with in for loop intendentation
    return total


print("Start")
print(multiply(1, 2, 3))

# for debuggin click on debug icon on the left side of the vscode
# creating a json file
#  break point can be creating by placing the cursol on the line and hitting F9
# pressing F5 to run the program upto the break point
# to execute one statement at a time press F10
# insteed of pressing F10 again press F11 which will take us to the funtion
# to stop the debugger press Shift + F5
