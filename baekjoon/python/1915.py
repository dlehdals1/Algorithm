n , m = map(int, input().split())

mat = [[0 for _ in range(m)] for _ in range(n)]
biggest_size = 0

for i in range(n):
    line = input()
    for j in range(m):
        if line[j] == "1":
            mat[i][j] = 1
            biggest_size = 1
            

for i in range(1,n):
    for j in range(1,m):
        if mat[i][j]:
            mat[i][j] = min(mat[i-1][j], mat[i][j-1], mat[i-1][j-1]) + 1
            if mat[i][j] >  biggest_size:
                biggest_size = mat[i][j]

print(biggest_size ** 2)
