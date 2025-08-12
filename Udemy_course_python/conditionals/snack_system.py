# A local cafe wants a program that suggests a snack.
# If a customer ask for a cookies or samosa, its confirms the order.
# othewise, it says it's not available

# TASK :

# -- take snack input
# -- If it't cookies or samosa, confirm order
# else show unavailability

snack_input = input("Enter you'r order: ").lower()

if snack_input == "cookies" or snack_input == "samosa":
    print("Ordered Confirmed!")

else:
    print("Not Available")
