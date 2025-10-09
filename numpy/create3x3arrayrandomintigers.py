import numpy as np

arr = np.random.randint(1, 50, size=(3, 3))
print("Original Array:\n", arr)

sorted_arr = np.sort(arr, axis=1)
print("Row-wise Sorted Array:\n", sorted_arr)