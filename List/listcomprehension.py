mixed_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
print(f"Original mixed list: {mixed_list}")

# Use list comprehension to filter for numbers (integers and floats)
# isinstance(item, (int, float)) checks if the item is an integer OR a float
numbers_only_list = [item for item in mixed_list if isinstance(item, (int, float))]

print(f"List containing only numbers: {numbers_only_list}")