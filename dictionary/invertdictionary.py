def invert_dictionary(input_dict):
  inverted_dict = {}
  # iterates through each key-value pair in the input_dict
  for key, value in input_dict.items():
    inverted_dict[value] = key
  return inverted_dict

original_dict1 = {'a': 1, 'b': 2, 'c': 3}

print(f"Original dictionary 1: {original_dict1}")
print(f"Inverted dictionary 1: {invert_dictionary(original_dict1)}")