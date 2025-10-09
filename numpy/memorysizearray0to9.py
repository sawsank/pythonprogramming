import numpy as np

arr = np.arange(10)
print("Array:", arr)
print("Memory size in bytes:", arr.nbytes)

"""Explanation: Each element in NumPy has a fixed size.
 nbytes gives the total memory used by the array"""