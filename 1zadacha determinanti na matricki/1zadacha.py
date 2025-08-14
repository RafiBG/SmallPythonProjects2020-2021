import numpy as np
row = int(input())
a = [[float(j) for j in input().split()] for i in range(row)]

detA = round(np.lina4lg.det(a),2)
print(detA)
