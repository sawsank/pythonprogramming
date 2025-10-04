def count_char_frequencies(input_string):
  frequency_dict = {}
  for char in input_string:
    # Use get() method: if char is in dict, get its value; otherwise, default to 0
    frequency_dict[char] = frequency_dict.get(char, 0) + 1
  return frequency_dict

string1 = 'Jessa'
print(f"Frequencies for '{string1}': {count_char_frequencies(string1)}")