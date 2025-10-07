def copy_binary_file(source_filename, destination_filename):
    try:
        with open(source_filename, 'rb') as source_file:
            binary_content = source_file.read()
        with open(destination_filename, 'wb') as destination_file:
            destination_file.write(binary_content)
        print(f"Successfully copied binary file '{source_filename}' to '{destination_filename}'.")
    except FileNotFoundError:
        print(f"Error: Source binary file '{source_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
source_binary_file = "filehandling/input.bin" # Make sure this binary file exists
destination_binary_file = "filehandling/output.bin"
copy_binary_file(source_binary_file, destination_binary_file)

"""
Explanation:

-The copy_binary_file function opens the source file in read binary mode ('rb').
-binary_content = source_file.read() reads the entire content of the binary file as a bytes object.
-Next, with open(destination_filename, 'wb') as destination_file: opens the destination file in write binary mode ('wb').
-destination_file.write(binary_content) writes the bytes read from the source file to the destination file.
"""