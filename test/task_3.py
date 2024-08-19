m = int(input())

n = int(input())

matrix = [[x for x in range(m)] for y in range(n)]

for i in range(m):
    for j in range(n):
        matrix[i][j] = int(input())

print([[element * 2 for element in row] for row in matrix])
