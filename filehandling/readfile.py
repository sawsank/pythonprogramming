try:
    with open("filehandling/sample.txt", 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: 'sample.txt' not found.")

    """
    with open("sample.txt", 'r') as file: opens the file named “sample.txt” in read mode. 
    The with statement ensures the file is automatically closed even if errors occur.

    content = file.read() method reads the entire content of the file as a single string and stores it in the content variable.
    
    At last the print(content) functions then displays the content on the console."""