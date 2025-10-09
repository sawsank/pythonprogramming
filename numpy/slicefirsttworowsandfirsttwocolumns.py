import numpy as np

arr = np.arange(1, 17).reshape(4, 4)
print("Array:\n", arr)

sub_arr = arr[0:2, 0:2]
print("First 2 rows and columns:\n", sub_arr)

""""Explanation:

arr[0:2, 0:2] → selects rows 0–1 and columns 0–1.
The result is a 2×2 sub-matrix."""