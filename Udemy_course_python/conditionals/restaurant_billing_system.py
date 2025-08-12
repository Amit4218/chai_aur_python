# Restaurant Billing System
#
# You’re designing a billing system for a restaurant. Depending on the total bill amount entered by the customer, they might get a free dessert.
#
#
# Tasks:
#
# If the bill amount is greater than 500, return the string "You get a free dessert!"
#
# Otherwise, return the string: "No free dessert this time."
#

bill_amount = int(input("Enter your bill: "))

if bill_amount > 500:
    print("You get a free dessert!")

else:
    print("No free dessert this time.")
