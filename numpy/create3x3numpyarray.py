import numpy as np

arr = np.ones((3, 3), dtype=bool)
print(arr)
"""Explanation: The np.full() function is a powerful way to create an array of any given shape filled with a specific value. 
The first argument (3, 3) specifies the shape (3 rows, 3 columns), and the second argument True is the value to fill the array with. 
The dtype=bool ensures that the array’s data type is boolean."""