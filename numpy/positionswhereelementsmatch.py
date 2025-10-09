import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, 4, 3, 7, 8])

# Use np.where() to find the index where the values match
index = np.where(a == b)
print(index)