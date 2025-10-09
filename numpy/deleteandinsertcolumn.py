import numpy as np

sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([10, 10, 10]) # Use a 1D array for simplicity

# Delete the second column (index 1)
# axis=1 specifies that the operation should be on columns
deletedArray = np.delete(sampleArray, 1, axis=1)

# Insert the new column at the second position (index 1)
# axis=1 specifies that we're inserting a column
resultArray = np.insert(deletedArray, 1, newColumn, axis=1)

print(resultArray)