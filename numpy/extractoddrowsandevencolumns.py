import numpy as np

# Original array
sampleArray = np.array([
    [3, 6, 9, 12], 
    [15, 18, 21, 24], 
    [27, 30, 33, 36], 
    [39, 42, 45, 48], 
    [51, 54, 57, 60]
])

# Use slicing to select odd rows and even columns
# The slice [1::2] selects every second element starting from index 1 (odd rows).
# The slice [::2] selects every second element starting from index 0 (even columns).
newArray = sampleArray[1::2, ::2]

print("Original Array:")
print(sampleArray)

print("\nNew Array with Odd Rows and Even Columns:")
print(newArray)

"""Explanation:

The syntax array[start:stop:step] lets you specify which elements to select.

1::2 for the rows means:

Start: at index 1 (the second row).
Stop: Omitted, so it goes to the end of the array.
Step: 2, meaning it selects every second row. This gives us rows at indices 1 and 3.
::2 for the columns means:

Start: Omitted, so it defaults to 0 (the first column).
Stop: Omitted, so it goes to the end.
Step: 2, meaning it selects every second column. This gives us columns at indices 0 and 2.
By combining these two slices, sampleArray[1::2, ::2], NumPy efficiently creates a new array containing the elements at the intersection of the specified rows and columns."""