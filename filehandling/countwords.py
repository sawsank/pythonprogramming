import re

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = re.findall(r'\b\w+\b', content) # Use regex to find whole words
            return len(words)
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
word_count = count_words("filehandling/sample1.txt")
print(f"Total words in 'sample1.txt': {word_count}")