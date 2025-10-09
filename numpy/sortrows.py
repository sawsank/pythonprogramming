import numpy as np

arr = np.array([[8, 4, 1],
                [5, 2, 7],
                [6, 9, 3]])

# Get the indices that would sort the second column
sorted_indices = arr[:, 1].argsort()

# Use the indices to sort the entire array's rows
sorted_arr = arr[sorted_indices]
print(sorted_arr)