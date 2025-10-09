import numpy as np

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 1]])

# Add the two arrays
resultArray = arrayOne + arrayTwo

print("Result of array addition:")
print(resultArray)

# Square each element of the resultArray
squaredArray = resultArray ** 2

print("\nResult with each element squared:")
print(squaredArray)