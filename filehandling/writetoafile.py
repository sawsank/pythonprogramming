filename = "filehandling/output.txt"
text_to_write = "Hello, shasank!"

try:
    with open(filename, 'w') as file:
        file.write(text_to_write)
    print(f"Successfully wrote '{text_to_write}' to '{filename}'.")
except Exception as e:
    print(f"An error occurred: {e}")