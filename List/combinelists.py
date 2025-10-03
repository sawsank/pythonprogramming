list_a = [1, 2]
list_b = [3, 4]

# Method 1: Using the + operator (creates a new list)
combined_list_plus = list_a + list_b
print("Combined list (using + operator):", combined_list_plus)

# Method 2: Using the extend() method (modifies list_a in-place)
temp_list = [1, 2]
temp_list.extend(list_b)
print("Combined list (using .extend() on temp_list):", temp_list)

# Method 3: Using unpacking (creates a new list - Python 3.5+)
combined_list_unpacking = [*list_a, *list_b]
print("Combined list (using unpacking *):", combined_list_unpacking)