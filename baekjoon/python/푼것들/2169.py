import sys

n, m = map(int, sys.stdin.readline().split())
mat = []
dp_left = [[float("-inf") for _ in range(m)] for _ in range(n)]
dp_down = [[float("-inf") for _ in range(m)] for _ in range(n)]
dp_right = [[float("-inf") for _ in range(m)] for _ in range(n)]
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

dp_down[0][0] = mat[0][0]
dp_left[0][0] = mat[0][0]
dp_right[0][0] = mat[0][0]

for i in range(n):
    for j in range(m):
        if i > 0:
            dp_down[i][j] = max(dp_down[i - 1][j], dp_left[i - 1][j], dp_right[i - 1][j]) + mat[i][j]
            dp_down[i][m - 1 - j] = max(dp_down[i - 1][m - 1 - j], dp_left[i - 1][m - 1 - j], dp_right[i - 1][m - 1 - j]) + mat[i][m - 1 - j]
            
        if j > 0:
            dp_left[i][j] = max(dp_down[i][j - 1], dp_left[i][j - 1]) + mat[i][j]    
            if i != 0:
                dp_right[i][m - 1 - j] = max(dp_down[i][m - j], dp_right[i][m - j]) + mat[i][m - 1 - j]

def print_mat(mat):
    print()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = " ")
        print()
    print()

print_mat(dp_down)
print_mat(dp_left)
print_mat(dp_right)

print(max(dp_down[i][j], dp_left[i][j]))