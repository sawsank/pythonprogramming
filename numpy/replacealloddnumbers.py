import numpy as np

arr = np.arange(1, 11)
print("Original Array:", arr)

arr[arr % 2 == 1] = -1
print("Modified Array:", arr)