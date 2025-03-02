string = "please don't repeat yourself "

for char in string:
    if char.count(char) == 1:
        print("char", char)
        break