import matmul

A = matmul.readm('A.csv')
b = matmul.readm('b.csv')

C = matmul.matmul(A, b)


for row in C:
    print(row)