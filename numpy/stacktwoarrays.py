import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

v_stack = np.vstack((a, b))
h_stack = np.hstack((a, b))

print("Vertical Stack:\n", v_stack)
print("Horizontal Stack:\n", h_stack)