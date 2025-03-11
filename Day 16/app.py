def caesar_cipher(message, shift, mode):
    """
    Encrypts or decrypts a message using the Caesar Cipher algorithm.

    Parameters:
        message (str): The input message to encrypt or decrypt.
        shift (int): The number of positions to shift each letter.
        mode (str): 'encrypt' or 'decrypt'.

    Returns:
        str: The encrypted or decrypted message.
    """
    result = ""
    shift = shift % 26  # Ensure the shift is within the range of 0-25

    for char in message:
        if char.isalpha():  # Only process alphabetic characters
            # Determine the base ASCII value for uppercase or lowercase letters
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo 26
            shifted_char = chr((ord(char) - base + (shift if mode == 'encrypt' else -shift)) % 26 + base)
            result += shifted_char
        else:
            result += char  # Non-alphabetic characters are added as-is

    return result

def main():
    print("🌟 Caesar Cipher Encoder & Decoder 🔐")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()

    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please choose 'encrypt' or 'decrypt'.")
        return

    result = caesar_cipher(message, shift, mode)
    print(f"Result: {result}")

# Run the program
if __name__ == "__main__":
    main()