import numpy as np

a = np.array([1, 2, 3, 2, 8, 4, 2, 4])
b = np.array([2, 4, 5, 6, 8])
common_items = np.intersect1d(a, b)
print(common_items)