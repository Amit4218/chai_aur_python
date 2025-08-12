users = [
    {"id": 1, "total": 178, "discount": "P20"},
    {"id": 2, "total": 269, "discount": "F50"},
    {"id": 3, "total": 118, "discount": "D10"},
]


discounts = {
    "P20": (0.2, 0),
    "F50": (0, 10),
    "D10": (0.5, 0),
}

for user in users:
    percent, fixed = discounts.get(user["discount"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]}: paid {user['total']}, and go a discount of {discount}")
