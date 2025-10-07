filename = "filehandling/output.txt"
text_to_append = " This is an appended line."

try:
    with open(filename, 'a') as file:
        file.write("\n" + text_to_append) # Adding a newline character for better readability
    print(f"Successfully appended '{text_to_append}' to '{filename}'.")
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")