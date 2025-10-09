import numpy as np

A = np.array([[4, 2],
              [1, 3]])

eigvals, eigvecs = np.linalg.eig(A)
print("Eigenvalues:\n", eigvals)
print("Eigenvectors (columns):\n", eigvecs)