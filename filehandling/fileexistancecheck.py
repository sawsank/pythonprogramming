"""The os.path.exists(filename) checks if the file specified by filename exists. 
It returns True if the file or directory exists, and False otherwise."""

import os

def check_file_exists(filename):
    return os.path.exists(filename)

# Example usage:
filename = "filehandling/sample.txt"
exists = check_file_exists(filename)
print(f"Does '{filename}' exist? {exists}")