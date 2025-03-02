items = ["apple", "banana", "mango", "apple", "grapes"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("duplicate item: ", item)
        break
    else:
        unique_items.add(item)