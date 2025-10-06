my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple with duplicates: {my_tuple}")

# Convert to a set to remove duplicates (order is not preserved)
unique_elements_set = set(my_tuple)

# Convert back to a tuple
unique_tuple = tuple(unique_elements_set)
print(f"Tuple with unique elements: {unique_tuple}")