import os

def rename_file(old_filename, new_filename):
    if not os.path.exists(old_filename):
        return f"Error: File '{old_filename}' not found."
    try:
        os.rename(old_filename, new_filename)
        return f"Successfully renamed '{old_filename}' to '{new_filename}'."
    except Exception as e:
        return f"An error occurred while renaming: {e}"

# Example usage:
old_name = "filehandling/old_file.txt"
new_name = "filehandling/new_file.txt"
result = rename_file(old_name, new_name)
print(result)