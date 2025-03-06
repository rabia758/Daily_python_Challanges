import re

# Function to analyze emoji sentiment
def analyze_mood(message):
    # Define emoji categories
    happy_emojis = ["😊", "😃", "😍"]
    sad_emojis = ["😢", "😭", "☹"]
    angry_emojis = ["😡", "🤬", "😠"]
    neutral_emojis = ["😐", "😶", "🤔"]

    # Check for emojis in the message
    emojis_in_message = re.findall(r"[^\w\s,]", message)

    if not emojis_in_message:
        return "No emoji found, can't detect mood! 🤷‍♂"

    # Detect mood based on emojis
    for emoji in emojis_in_message:
        if emoji in happy_emojis:
            return "Happy Mood! 🎉"
        elif emoji in sad_emojis:
            return "Sad Mood! 😢"
        elif emoji in angry_emojis:
            return "Angry Mood! 😠"
        elif emoji in neutral_emojis:
            return "Neutral Mood! 😐"

    return "Emoji found, but mood couldn't be determined. 🤔"

# Main function
def main():
    # User input
    message = input("Enter your message: ")
    # Analyze mood
    result = analyze_mood(message)
    # Display result
    print(f"Detected Mood: {result}")

# Run the program
if __name__ == "__main__":
    main()
    
