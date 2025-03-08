def encrypt(message, shift=3):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Ensure shift is within 26 letters
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  # Keep non-alphabetic characters as is
    return encrypted_message

def decrypt(encrypted_message, shift=3):
    return encrypt(encrypted_message, -shift)  # Decrypt by shifting backward

# Main program
if __name__ == "__main__":
    message = input("Enter your message: ")
    encrypted = encrypt(message)
    decrypted = decrypt(encrypted)

    print(f"\nOriginal Message: {message}")
    print(f"Encrypted Message: {encrypted}")
    print(f"Decrypted Message: {decrypted}")