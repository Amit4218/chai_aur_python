while True: 

    age = int(input("Enter your age: "))

    if(age < 13):
        print("You are a child ")
    elif age < 20:
        print("teenager")
    elif age < 60:
        print("adult")
    else:
        print("senior")