fruit = "Banana"
color = str(input("Enter color of the fruit: ")).capitalize()

if color == "Green":
    ripe = "unripe"
elif color == "Yellow":
    ripe = "Ripe"
elif color == "Brown":
    ripe = "overripe"
else:
    print("Invalid input !")    

print(f"Your {fruit} is {ripe}")