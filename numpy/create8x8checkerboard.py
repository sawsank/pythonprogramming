import numpy as np

# Create an 8x8 array of zeros
checkerboard = np.zeros((8, 8), dtype=int)

# Use slicing and a step of 2 to set alternating elements
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print(checkerboard)