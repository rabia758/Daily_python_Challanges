import random
import string

def generate_password(length):
    """
    Generates a secure random password of the specified length.
    Includes uppercase, lowercase, numbers, and special characters.
    """
    # Define character sets
    uppercase_letters = string.ascii_uppercase  # A-Z
    lowercase_letters = string.ascii_lowercase  # a-z
    digits = string.digits  # 0-9
    special_characters = string.punctuation  # !@#$%^&*() etc.

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password to make it more random
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def main():
    print("🌟 Random Password Generator 🔐")
    try:
        # Get the desired password length from the user
        length = int(input("Enter the desired password length (minimum 4): "))
        if length < 4:
            print("Password length must be at least 4 characters.")
        else:
            # Generate and display the password
            password = generate_password(length)
            print(f"Your secure password is: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Run the program
if __name__ == "__main__":
    main()