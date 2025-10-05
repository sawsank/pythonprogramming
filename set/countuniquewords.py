sentence = "dog is a simple animal dogs is selfless animal"

# Convert the sentence to lowercase and split it into words
words = sentence.lower().split()

# Convert the list of words to a set to get unique words
unique_words = set(words)

# Count the number of unique words
unique_word_count = len(unique_words)

print(f"Original sentence: '{sentence}'")
print(f"Number of unique words: {unique_word_count}")