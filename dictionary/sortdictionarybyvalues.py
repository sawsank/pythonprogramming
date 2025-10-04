from collections import OrderedDict

my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
print(f"Original dictionary: {my_dict}")

# Method 1: Create an OrderedDict sorted by values
print("\nSorted by values (as OrderedDict):")
sorted_by_value_ordered_dict = OrderedDict(my_dict)
print(sorted_by_value_ordered_dict)

# Method 2: Convert to a list of (key, value) tuples, sorted by value
print("\nSorted by values (as list of tuples):")
print(my_dict)