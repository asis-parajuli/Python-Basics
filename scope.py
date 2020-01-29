# scope is the region of the code where the varibale is defined

message = "a"  # this is a global variable
# global varibale stay in the memory for a longer period of time unless they are garbage collected


def greet():
    message = "a"


# we get a error on the message becuase it is defined inside the greet function and cannot be used outside
print(message)


def send_email(name):
    message = "b"

# we can used the argument name in another function outside of the greet function
