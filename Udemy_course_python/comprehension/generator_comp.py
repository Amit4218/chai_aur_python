random_numbers = [1, 2, 3, 56, 7, 5, 4, 6976, 6, 5343, 94, 57]

number = sum(num for num in random_numbers if num % 2 == 0)
print(number)
