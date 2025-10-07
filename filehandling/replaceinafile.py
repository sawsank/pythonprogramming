def replace_in_file(source_filename, destination_filename, old_word, new_word):
    try:
        with open(source_filename, 'r') as source_file:
            content = source_file.read()
        modified_content = content.replace(old_word, new_word)
        with open(destination_filename, 'w') as destination_file:
            destination_file.write(modified_content)
        return f"Successfully replaced '{old_word}' with '{new_word}' in '{source_filename}' and saved to '{destination_filename}'."
    except FileNotFoundError:
        return f"Error: Source file '{source_filename}' not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
source_file = "filehandling/sample2.txt"
destination_file = "filehandling/replaced_file.txt"
word_to_replace = "old"
replacement_word = "new"

# Create a dummy file to test replacement
with open(source_file, 'w') as f:
    f.write("This is an old file with some old content.")

result = replace_in_file(source_file, destination_file, word_to_replace, replacement_word)
print(result)