import numpy as np

arr = np.arange(10)
print("Original Array:", arr)

np.random.shuffle(arr)
print("Shuffled Array:", arr)