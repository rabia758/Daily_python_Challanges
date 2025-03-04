import re

def check_password_strength(password):
    # Weak: Agar password 6 characters se chhota hai ya sirf alphabets hain
    if len(password) < 6 or password.isalpha():
        return "Weak ❌"

    # Moderate: Agar password 8+ characters ka hai lekin koi special character nahi hai
    if len(password) >= 8 and re.search(r"[A-Za-z]", password) and re.search(r"[0-9]", password):
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "Moderate ⚠"

    # Strong: Agar password 8+ characters, uppercase, lowercase, number, aur special character sab kuch contain karta hai
    if len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and re.search(r"[0-9]", password) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Strong ✅"

    return "Weak ❌"

def password_strength_checker():
    attempts = 3
    for _ in range(attempts):
        password = input("Enter your password: 🔑 ")
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")
        if strength == "Strong ✅":
            break
        elif strength != "Strong ✅" and _ < attempts - 1:
            print(f"Please try again. You have {attempts - _ - 1} attempts left. 🔄")
    else:
        print("Make your password powerfully! 💪")

# Program ko start karein
password_strength_checker()
