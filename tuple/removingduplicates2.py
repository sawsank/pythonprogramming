from collections import OrderedDict
my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(f"Original tuple with duplicates: {my_tuple}")

unique_ordered_tuple = tuple(OrderedDict.fromkeys(my_tuple))
print(f"Tuple with unique elements (order preserved): {unique_ordered_tuple}")