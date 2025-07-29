# A tea stall offers different prices for different cup sizes.
# Write a program that calculates the price based on the size

# Task :
#
# -- Input : "small", "medium", "large"
# -- small -> $10 Meduim -> $15 large -> $20
# -- if invalid : show "Unknown cup size"


tea_size = input("Enter you'r cup size: ").lower()

if tea_size == "small":
    print("$10")
elif tea_size == "medium":
    print("$15")
elif tea_size == "large":
    print("$20")
else:
    print("Unknown cup size")
