from functools import wraps  # see line 31 for this

# Syntax:

# def decorator_name(func: # this function will take a function as an argument):
#   def wrapper(): # A wrapper function inside the decoratoe()
#       fun() # we call the recived function intide the wrapper
#   return wrapper

# we can use the decorator using the '@' symbol

# Example:


def decorator(function):
    def wrapper():
        print("Inside the wrapper")
        function()
        print("After function is executed")

    return wrapper


@decorator
def greet():
    print("This is greet function")


greet()
print(f"This is without warps decorator (defination name): {greet.__name__}")

# But when doing this sometimes we lose the meta data for that we can import warp from functools

# Example:

# print(greet.__name__) if we do this we will get wrapper as the name of the function, which is not true
# We can solve that by using the warps and decorating the wraper with it.


def decorator_2(function_2):
    @wraps(function_2)
    def wrapper_2():
        print("Inside the wrapper")
        function_2()
        print("After function is executed")

    return wrapper_2


@decorator_2
def greeting():
    print("This is greeting function")


greeting()
print(f"This is with warps decorator (defination name): {greeting.__name__}")
