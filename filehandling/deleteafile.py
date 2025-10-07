import os

def delete_file(filename):
    if not os.path.exists(filename):
        return f"Error: File '{filename}' not found."
    try:
        os.remove(filename)
        return f"Successfully deleted '{filename}'."
    except Exception as e:
        return f"An error occurred while deleting: {e}"

# Example usage:
file_to_delete = "filehandling/temp_file.txt"

# Create a dummy file to test deletion
with open(file_to_delete, 'w') as f:
    f.write("This file will be deleted.")

result = delete_file(file_to_delete)
print(result)