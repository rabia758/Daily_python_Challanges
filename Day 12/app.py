def Check_Password (password):
    length = len(password)

    digit = any(char.isdigit() for char in password)
    uppercase = any(char.isupper() for char in password)
    special = any(char in "!@#$%^&*()_+" for char in password)

    if length < 6:
        return "your password strength is weak ❌"
    elif length <= 10:
        if digit:
            return "your password strength is medium ⚠ "
        else:
            return "your password strngth is weak"
    else :
        if digit and uppercase and special:
            return "your password strength is strong ✅"
        else:
            return "your password strength is medium ⚠"

password =input("Enter Your Password: ") 
result = Check_Password(password)       
print (result)
