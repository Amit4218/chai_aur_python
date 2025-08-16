orders = [
    "Masala Chai",
    "Green Tea",
    "Iced Green Tea",
    "Milk Tea",
    "Masala Chai",
    "Green Tea",
]

my_order = {order for order in orders}
print(my_order)

chai_ingredients = {
    "masala":["Masala","milk","tea_leaves"],
    "lemon": ["water","tea_leaves"],
    "normal":["milk","tea_leaves","sugar"]
}

my_chai = { unique_ingre for ingredients in chai_ingredients.values() for unique_ingre in ingredients}
print(my_chai)