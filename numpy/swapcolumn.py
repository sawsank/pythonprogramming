import numpy as np

arr = np.arange(9).reshape(3, 3)
print("Before")
print(arr)
# The columns are at index 0, 1, 2. We want to rearrange to 0, 2, 1

arr[:, [1, 2]] = arr[:, [2, 1]]
print("After")
print(arr)