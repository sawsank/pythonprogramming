def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i + 1):
            print(i, end=" ")
        print()
print_pattern(5)
print_pattern(10)