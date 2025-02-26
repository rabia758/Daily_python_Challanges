def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} Yes, it's a prime number!")
else:
    print(f"{num} No, it's not a prime number.")