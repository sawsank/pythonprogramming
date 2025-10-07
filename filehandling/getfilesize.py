import os

def get_file_size(filename):
    try:
        size_in_bytes = os.path.getsize(filename)
        return size_in_bytes
    except FileNotFoundError:
        return f"Error: '{filename}' not found."

# Example usage:
filename = "filehandling/sample1.txt"
size = get_file_size(filename)
print(f"The size of '{filename}' is: {size} bytes.")