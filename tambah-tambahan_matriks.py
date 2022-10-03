# Mariks A + Matriks B
A = [
    [5, 3],
    [3, 4],
]

B = [
    [6, 3],
    [7, 3],
]
for i in range(0, len(A)):
    for j in range(0, len(A[0])):
        print (A[i][j] + B[i][j], end=' '),
    print	()