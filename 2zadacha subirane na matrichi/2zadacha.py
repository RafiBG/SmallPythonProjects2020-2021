import csv
import numpy as np

with open('file1.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

sizeA = int(data[0][0])
matrixA = np.array(data[1:(sizeA)+1])
matrixA = matrixA.astype(np.float)

sizeB = int(data[sizeA+1][0])
matrixBStartIndex = sizeA+2
matrixB = np.array(data[matrixBStartIndex:])
matrixB = matrixB.astype(np.float)

result = matrixA + matrixB
print(result)

with open('file2.csv',newline='')as f:
    reader = csv.reader(f)
    data = list(reader)

sizeC = int(data[0][0])
matrixC = np.array(data[1:(sizeC)+1])
matrixC = matrixC.astype(np.float)

sizeD = int(data[sizeA+1][0])
matrixDStartIndex = sizeC+2
matrixD = np.array(data[matrixDStartIndex:])
matrixD = matrixD.astype(np.float)

result2 = matrixC + matrixD
print(result2)