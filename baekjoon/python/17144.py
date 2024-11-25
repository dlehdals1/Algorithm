import sys
r, c, t = map(int, sys.stdin.readline().split())

mat = []
new_mat = [[0 for _ in range(c)] for _ in range(r)]
dusts = []
new_dust = []
vac = []


def print_mat(matrix):
    print("mat print")
    for i in range(r):
        print(*matrix[i])

def spread(x, y):
    count = 0
    if mat[x][y] >= 5:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dir in dirs:
            nx = x + dir[0]
            ny = y + dir[1]
            if 0 <= nx < r and 0 <= ny < c and mat[nx][ny] > -1:
                count += 1
                new_mat[nx][ny] += mat[x][y] // 5
                new_dust.append([nx, ny])
                
    new_dust.append([x, y])
    new_mat[x][y] += mat[x][y] - count * (mat[x][y] // 5)

def push_dust():
    for i in range(vac[0][0] - 1, 0, -1):
        mat[i][0] = mat[i - 1][0]
    for i in range(0, c - 1):
        mat[0][i] = mat[0][i + 1]
    for i in range(0, vac[0][0]):
        mat[i][c - 1] = mat[i + 1][c - 1]
    for i in range(c - 1, 1, -1):
        mat[vac[0][0]][i] = mat[vac[0][0]][i - 1]
    mat[vac[0][0]][1] = 0
    mat[vac[0][0]][0] = -1

    for i in range(vac[1][0] + 1, r - 1):
        mat[i][0] = mat[i + 1][0]
    for i in range(0, c - 1):
        mat[r - 1][i] = mat[r - 1][i + 1]
    for i in range(r - 1, vac[1][0], -1):
        mat[i][c - 1] = mat[i - 1][c - 1]
    for i in range(c - 1, 1, -1):
        mat[vac[1][0]][i] = mat[vac[1][0]][i - 1]
    mat[vac[1][0]][1] = 0
    mat[vac[1][0]][0] = -1

    for i in range(r):
        for j in range(c):
            if mat[i][j] > 0:
                dusts.append([i, j])

for i in range(r):
    mat.append(list(map(int, sys.stdin.readline().split())))
    for j in range(c):
        if mat[i][j] > 0:
            dusts.append([i,j])
        if mat[i][j] < 0:
            vac.append([i,j])
for _ in range(t):
    for dust in dusts:
        spread(dust[0],dust[1])
    mat = new_mat
    new_mat = [[0 for _ in range(c)] for _ in range(r)]
    dusts = []
    new_dust = []
    push_dust()


count_dust = 0
for i in range(r):
    for j in range(c):
        if mat[i][j] > 0:  
            count_dust += mat[i][j]
print(count_dust)