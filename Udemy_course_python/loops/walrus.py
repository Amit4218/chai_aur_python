choices = ["yes", "no", "y", "n", "Y", "N"]

if (user_choice := input("Enter your choice: ")) not in choices:
    print("ohh no")

else:
    print("Great choice!")


flavor = ["masala", "mint", "green"]

while (usr_inp := input("Enter ur flavor: ")) not in flavor:
    print("not availablel")
else:
    print(f"{flavor} is our best flavor")
