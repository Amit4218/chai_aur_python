# function with **Kwargs
# Create a function that any number of keywords arguments and
# print them in the format key: value

def key_value(**kwargs):
    for key, value in kwargs.items():
       print(f"{key}: {value}")
    

print(key_value(a=5, b=4))
print(key_value(name="amit", age=20, surname="bhagat"))
