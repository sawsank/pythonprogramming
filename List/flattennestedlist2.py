## Alternative and often more Pythonic using list comprehension
def flatten_list_comprehension(nested_list):
  return [item for sublist in nested_list for item in sublist]

# Test cases
list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
print(f"Original nested list: {list_of_lists}")

flattened_result_comp = flatten_list_comprehension(list_of_lists)
print(f"Flattened list (using list comprehension): {flattened_result_comp}")