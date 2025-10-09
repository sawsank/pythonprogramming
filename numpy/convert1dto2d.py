import numpy as np

arr = np.arange(6)
print("Original Array: ",arr)
arr_2d = arr.reshape(2, 3)
print("Reshaped 2x3 Array: ")
print(arr_2d)

"""Explanation: The .reshape() method is used to give a new shape to an array without changing its data.
 We specify the new shape as a tuple (rows, columns). 
 Since we want 2 rows and the original array has 6 elements, 
 the new array must have 5 columns (2 * 3 = 6)."""