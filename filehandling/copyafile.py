def copy_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'r') as source_file:
            content = source_file.read()
        with open(destination_filename, 'w') as destination_file:
            destination_file.write(content)
        print(f"Successfully copied '{source_filename}' to '{destination_filename}'.")
    except FileNotFoundError:
        print(f"Error: Source file '{source_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_file = "filehandling/sample1.txt"
destination_file = "filehandling/copied_sample.txt"
copy_file(source_file, destination_file)