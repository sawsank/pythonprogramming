import numpy as np

arr = np.array([1, 0, 2, 0, 3, 0, 4])
print("Array:", arr)

indices = np.nonzero(arr)
print("Indices of non-zero elements:", indices)

"""
Explanation:

np.nonzero(arr) returns a tuple of indices where elements are non-zero.
In this example → (array([0, 2, 4, 6]),) meaning non-zero elements are at positions 0, 2, 4, 6.
"""