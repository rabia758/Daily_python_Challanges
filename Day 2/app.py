# ----Day 2 Challange------
user_input = input("Enter Your Sentence: ")
words = user_input.split()
words_count = len(words)
print(f"{user_input.upper()} Number of Words: ", words_count ,"\n")


# Bonus Challenge (Optional)

words = user_input.split()
reverse_text = words.reverse()
reverse_text = ' '.join(words)
print(f"Reverse Text Is : {reverse_text}","\n")
