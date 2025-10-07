def count_specific_word(filename, word):
    try:
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = content.split()
            count = 0
            for w in words:
                # Remove punctuation to ensure accurate matching
                cleaned_word = w.strip('.,!?"\'()[]{};:')
                if cleaned_word == word.lower():
                    count += 1
            return count
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
filename = "filehandling/sample1.txt"
word_to_count = "the"
occurrences = count_specific_word(filename, word_to_count)
print(f"The word '{word_to_count}' appears {occurrences} times in '{filename}'.")