import numpy as np

arr = np.array([10, 20, 30, 40, 50])
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print("Normalized Array:", normalized)

"""Explanation:

Subtract the minimum value so the smallest becomes 0.
Divide by the range (max - min) so the largest becomes 1.
This scales all values into [0, 1]."""