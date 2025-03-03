import random

def number_guessing_game():
    print("🚀 Welcome to the Number Guessing Game! 🎯")
    print("Enter a number between 1 and 100.")
    
    # Random number generate karein
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Guess the number (between 1 and 100): 🔢 "))
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again. ⬇️")
        elif guess > number_to_guess:
            print("Too high! Try again. ⬆️")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts! 🎉✅")
            break

# Game ko start karein
number_guessing_game()
