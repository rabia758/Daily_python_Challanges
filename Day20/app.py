import random

# Flashcar"ds data
flashcards = {
    "What is the output of print(2 ** 3)?": "8",
    "What is the capital of France?": "Paris",
    "What is 5 + 7?": "12",
    "What is the largest planet in the solar system?": "Jupiter",
    "What is the square root of 64?": "8"
}

def show_flashcard():
    # Pick a random question
    question = random.choice(list(flashcards.keys()))
    print(f"📌 Question: {question}")

    # Wait for user to press Enter to show the answer
    input("Press Enter to show the answer...")
    print(f"📌 Answer: {flashcards[question]}\n")

def main():
    print("Welcome to the Python Flashcards App! 🎉")
    while True:
        show_flashcard()
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()