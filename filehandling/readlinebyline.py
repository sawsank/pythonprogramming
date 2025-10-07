try:
    with open("filehandling/sample1.txt", 'r') as file:
        for line in file:
            print(line, end='') # The 'end=''' prevents extra newline characters
except FileNotFoundError:
    print("Error: 'sample1.txt' not found.")