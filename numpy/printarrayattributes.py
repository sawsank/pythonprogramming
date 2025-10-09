import numpy as np

# Create the 4x2 array of type unsigned int16
# We use np.array() and specify the dtype
my_array = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint16)

# Print the attributes
print("The shape of the array is:", my_array.shape)
print("The number of dimensions is:", my_array.ndim)
print("The size of each element in bytes is:", my_array.itemsize)

"""Explanation: np.array() converts a Python list into a NumPy array. 
This allows efficient mathematical operations."""