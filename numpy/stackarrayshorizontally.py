import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
stacked_arr = np.hstack((a, b))
print(stacked_arr)

"""Explanation: The np.hstack() function stands for “horizontal stack.” 
It stacks arrays in sequence column-wise, effectively concatenating them along the second axis. 
For 1D arrays, this simply joins them end-to-end."""