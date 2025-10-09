import numpy as np

arr = np.arange(1, 17).reshape(4, 4)
print("Array:\n", arr)

first_row = arr[0]
print("First Row:", first_row)

last_col = arr[:, -1]
print("Last Column:", last_col)

"""Explanation:

np.arange(1, 10).reshape(3, 3) creates a 3×3 array with numbers 1–9.
arr[0] selects the first row (indexing starts at 0)."""