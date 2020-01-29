def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


# two types of functions
# 1 - perform a task
# 2 - return a value
def get_greeting(name):
    return f"hi {name}"


message = get_greeting("Aashish")
file = open("content.txt", "w")
file.write(message)

# none is an object that returns the absence of a value
