"""
Q6. Nested List: Matrix Addition (Medium–High) 
Add two 2×2 matrices. 
"""

A = [[1, 2], [3, 4]] # matrix A
B = [[5, 6], [7, 8]] # matrix B
C = [[0, 0], [0, 0]] # final matrix

for i in range(2):
  for j in range(2):
    C[i][j] = A[i][j] + B[i][j]

print(C)