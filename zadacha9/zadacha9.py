import numpy as np

A = np.array([-3, 7, 2])
B = np.array([10, -2, -7])
scalar_product = A.dot(B.T)
if scalar_product < 90:
    print('1')
elif scalar_product > 90:
    print('-1')
elif scalar_product == 90:
    print('0')
