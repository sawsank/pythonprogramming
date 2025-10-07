def count_characters(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return len(content)
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
char_count = count_characters("filehandling/sample1.txt")
print(f"Total characters in 'sample1.txt': {char_count}")