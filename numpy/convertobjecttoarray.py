import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Create an empty object array with the same size
obj_arr = np.empty(arr.size, dtype='object')

# Assign the elements from the original array
obj_arr[:] = arr

# We can now add a string element to it
obj_arr[1] = 'a'
print(obj_arr)
print(obj_arr.dtype)