import string
import getpass
import random


def check_password_strength(password: str) -> list:

    errors: list = []

    if len(password) < 7:
        errors.append("Password must be at least 8 characters long")
    if not any(char.islower() for char in password):
        errors.append("Password must contain atleast one lower case character")
    if not any(char.isupper() for char in password):
        errors.append("Password must contain atleast one upper case character")
    if not any(char.isdigit() for char in password):
        errors.append("Password must contain atleast one digit")
    if not any(char in string.punctuation for char in password):
        errors.append("Password must contain atleast one special character")

    return errors


def generate_strong_password(pass_length: int) -> str:

    characters = string.ascii_letters + string.digits + string.punctuation

    gen_pass = "".join(random.choice(characters) for _ in range(pass_length))

    return gen_pass


user_pass = getpass.getpass("Enter Your password: ")

errors = check_password_strength(user_pass)

if errors:
    print("Weak Password")
    for error in errors:
        print(error)

    print(f"Generated Pass: {generate_strong_password(pass_length=12)}")

else:

    print("Strong Password")

    choice = input("Do you still want suggested password (y/n): ").lower()
    pass_length = int(input("Enter the lenght of the pass you want (min 8): "))

    if choice == "y":
        if pass_length > 7:
            print(f"Generated Pass: {generate_strong_password(pass_length)}")
        else:
            print("Lenght must be greater than 8")
    else:
        print("Invalid Choice")
