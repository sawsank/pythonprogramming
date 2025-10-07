try:
    with open("filehandling/sample1.txt", 'r') as file:
        for i in range(5): # Adjust the range for the number of lines you want to read
          print(file.readline().strip())
except FileNotFoundError:
    print("Error: 'sample1.txt' not found.")