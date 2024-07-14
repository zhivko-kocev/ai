m = int(input())

n = int(input())

matrix = [[x for x in range(m)] for y in range(n)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input())

matrix = [[matrix[i][j] * 2 if i < n/2 else matrix[i][j]*3 for j in range(n)] for i in range(m)]

print(matrix)