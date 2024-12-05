import sys
n = int(sys.stdin.readline())

def make_star(n):
    if n == 1:
        return [["*"]]
    size = 4 * n -3
    mat = [[" " for _ in range(size)] for _ in range(size)]

    for i in range(size):
        mat[0][i] = "*"
        mat[i][0] = "*"
        mat[size - 1][i] = "*"
        mat[i][size - 1] = "*"
    
    small_mat = make_star(n - 1)

    for i in range(2,size - 2):
        for j in range(2,size - 2):
            mat[i][j] = small_mat[i-2][j-2]

    return mat
mat = make_star(n)
for i in range(4 * n - 3):
    print(*mat[i], sep="")