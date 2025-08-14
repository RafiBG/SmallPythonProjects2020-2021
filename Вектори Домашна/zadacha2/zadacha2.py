import numpy as np

A = np.array([2, 3, -2])
B = np.array([1, 6, 0])
AB = B - A
BALength = np.linalg.norm(AB)
print(AB)
print(BALength)