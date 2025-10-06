def get_min_max(numbers):
    if not numbers:
        return (None, None) # Handle empty list case
    
    min_val = min(numbers)
    max_val = max(numbers)
    return (min_val, max_val)

# Test the function
my_numbers = [10, 5, 20, 2, 15]
min_max_values = get_min_max(my_numbers)
print(f"Original numbers: {my_numbers}")
print(f"Minimum and maximum values: {min_max_values}")