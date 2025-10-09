import numpy as np

sampleArray = np.array([[34, 43, 73], [82, 22, 12], [53, 94, 66]])

# Get the indices that would sort the array by its second column
sorted_indices = sampleArray[:, 1].argsort()

# Use the sorted indices to reorder the rows of the array
sorted_array = sampleArray[sorted_indices]

print("Original array:")
print(sampleArray)

print("\nSorted array:")
print(sorted_array)