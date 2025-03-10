def start_game():
    print("🌟 Welcome to the Text-Based Adventure Game! 🌟")
    print("You find yourself in a dark forest. The path splits into two directions.")
    print("Do you go LEFT or RIGHT?")
    
    choice = input("Enter your choice (LEFT/RIGHT): ").strip().upper()
    
    if choice == "LEFT":
        left_path()
    elif choice == "RIGHT":
        right_path()
    else:
        print("Invalid choice! Please try again.")
        start_game()

def left_path():
    print("\nYou chose the LEFT path.")
    print("You encounter a mysterious cave. Do you ENTER or IGNORE it?")
    
    choice = input("Enter your choice (ENTER/IGNORE): ").strip().upper()
    
    if choice == "ENTER":
        print("\nYou enter the cave and find a treasure chest! 🎉")
        print("Congratulations, you win! 🏆")
    elif choice == "IGNORE":
        print("\nYou ignore the cave and continue walking.")
        print("Suddenly, a wild bear attacks you! 🐻")
        print("Game Over. 😢")
    else:
        print("Invalid choice! Please try again.")
        left_path()

def right_path():
    print("\nYou chose the RIGHT path.")
    print("You come across a river. Do you SWIM or LOOK for a bridge?")
    
    choice = input("Enter your choice (SWIM/LOOK): ").strip().upper()
    
    if choice == "SWIM":
        print("\nYou try to swim across the river but get swept away by the current. 🌊")
        print("Game Over. 😢")
    elif choice == "LOOK":
        print("\nYou find a hidden bridge and cross the river safely.")
        print("On the other side, you discover a magical kingdom! 🏰")
        print("Congratulations, you win! 🏆")
    else:
        print("Invalid choice! Please try again.")
        right_path()

# Start the game
start_game()