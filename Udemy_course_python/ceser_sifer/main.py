def encrypt(message, key):

    result = ""

    for char in message:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shifted = (ord(char) - base + key) % 26 + base
            result += chr(shifted)
        else:
            result += char

    return result


def decrypt(message, key):
    return encrypt(message, -key)


choice = (
    input("Enter E for (message encyption) or D for (message decryption) (E/D):  ")
    .lower()
    .strip()
)

if choice == "e":
    user_message = input("Enter your messages: ")
    key = int(input("Enter the encryption key: (1-25): "))
    encrypted = encrypt(user_message, key)
    print("Encrypted message: ", encrypted)

elif choice == "d":
    user_message = input("Enter your messages: ")
    key = int(input("Enter the decryption key: (1-25): "))
    decrypted = decrypt(user_message, key)
    print("Decrypted message: ", decrypted)

else:
    print("Invalid choice")
