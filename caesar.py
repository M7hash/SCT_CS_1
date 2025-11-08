# Caesar Cipher Program
# Allows user to Encrypt or Decrypt a message

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # non-alphabetic characters remain same
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

print("=== Caesar Cipher Program ===")

choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g. 3): "))

if choice == 'e':
    encrypted_text = encrypt(message, shift)
    print("\nEncrypted Message:", encrypted_text)
elif choice == 'd':
    decrypted_text = decrypt(message, shift)
    print("\nDecrypted Message:", decrypted_text)
else:
    print("Invalid choice! Please enter 'E' or 'D'.")

