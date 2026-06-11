def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            result += encrypted_char
        else:
            result += char

    return result


while True:
    print("\n===== Caesar Cipher Tool =====")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        message = input("Enter Message: ")
        shift = int(input("Enter Shift Value: "))
        encrypted = caesar_cipher(message, shift, "encrypt")
        print("Encrypted Message:", encrypted)

    elif choice == "2":
        message = input("Enter Encrypted Message: ")
        shift = int(input("Enter Shift Value: "))
        decrypted = caesar_cipher(message, shift, "decrypt")
        print("Decrypted Message:", decrypted)

    elif choice == "3":
        print("Program Closed Successfully!")
        break

    else:
        print("Invalid Choice!")