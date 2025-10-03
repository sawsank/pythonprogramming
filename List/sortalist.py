numbers = [5, 2, 8, 1, 9]
print("Original list:", numbers)

# Method 1: Using the sort() method (sorts in-place)
numbers.sort()
print("Sorted list (in-place using .sort()):", numbers)

# Resetting for demonstration of sorted()
numbers = [5, 2, 8, 1, 9]
print("\nOriginal list for sorted() demonstration:", numbers)

# Method 2: Using the sorted() function (returns a new sorted list)
sorted_numbers = sorted(numbers)
print("New sorted list (using sorted()):", sorted_numbers)
print("Original list after sorted() (unchanged):", numbers)