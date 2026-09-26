#python program to create array and perform addition of two matrices
import numpy as np
r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))

A = []
B = []

print("Enter the elements of the first matrix:")
for i in range(r):
    row = []
    for j in range(c):
        x = int(input("Enter A[" + str(i+1) + "][" + str(j+1) + "]: "))
        row.append(x)
    A.append(row)

print("Enter the elements of the second matrix:")
for i in range(r):
    row = []
    for j in range(c):
        x = int(input("Enter B[" + str(i+1) + "][" + str(j+1) + "]: "))
        row.append(x)
    B.append(row)

A = np.array(A)
B = np.array(B)
C = A + B
print("\nMatrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nAddition of A and B:")
print(C)