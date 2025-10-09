import numpy as np

# Create a random 3x2 matrix (values between 0 and 1)
matrix = np.random.rand(3, 2)

# Display the matrix
print("Matrix:\n", matrix)

# Find the maximum and minimum values
max_value = np.max(matrix)
min_value = np.min(matrix)

print("\nMaximum value:", max_value)
print("Minimum value:", min_value)
