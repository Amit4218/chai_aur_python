# Syntax:
# 
# variable = [expression iterable condition]

menu = [
    "Masala Chai",
    "Green Tea",
    "Iced Green Tea",
    "Milk Tea"
]

my_tea = [tea for tea in menu if "Milk" in tea] 

print(my_tea)