# create a function thats greets a user,
# if no name is given, it sould greet with defaut name

def greet(name = "default_value"):
    return "hello " + name


print(greet())
print(greet("amit"))