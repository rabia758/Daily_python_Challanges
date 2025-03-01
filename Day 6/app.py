# User se input lein
number = int(input("Enter your Number: 🔢 "))

# Number ko binary me convert karein
binary_representation = bin(number)[2:]  # bin() function "0b" prefix deta hai, isliye hum [2:] se usko hatate hain

# Binary representation ko check karein ke wo palindrome hai ya nahi
is_palindrome = binary_representation == binary_representation[::-1]

# Result dikhayein
print(f"Binary: {binary_representation} 🔢")

if is_palindrome:
    print("Output: Palindrome ✅ 🎉")
else:
    print("Output: Not a Palindrome ❌")