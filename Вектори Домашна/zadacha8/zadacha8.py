import numpy as np

A = np.array([4, 1, 4])
B = np.array([5, -2, 6])
scalar_product = A.dot(B.T)
if scalar_product > 0:
    print('yes')
    print(scalar_product)
else:
    print('no')
    print(scalar_product)