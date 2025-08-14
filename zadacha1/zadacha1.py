import numpy as np

A = np.array([3, 5, 6])
B = np.array([8, 4, 2])
AB = B - A
print(AB)
BA = A - B
print(BA)

C = np.array([8, 4, 2])
D = np.array([3, 5, 6])
CD = D - C
print()    #празния принт го сложих за разтояние между двете 
print(CD)
DC = C - D
print(DC)