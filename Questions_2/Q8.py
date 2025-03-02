number = 1
is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            print("Number is not prime")
            break
        else:
            print("Number is prime")
else:
    print("enter a value greater than 1")



