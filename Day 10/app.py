import re

def is_anagram(word1, word2):
    # Remove spaces, special characters, and convert to lowercase
    word1 = re.sub(r'[^a-zA-Z]', '', word1).lower()
    word2 = re.sub(r'[^a-zA-Z]', '', word2).lower()
    
    # Sort the letters and compare
    return sorted(word1) == sorted(word2)

# Input from the user
word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

# Check if they are anagrams
if is_anagram(word1, word2):
    print("Yes, it's an anagram! ✅")
else:
    print("No, it's not an anagram! ❌")

