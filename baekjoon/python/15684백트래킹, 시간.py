import sys

n, m, h = map(int, sys.stdin.readline().split())
mat = [[0 for _ in range(n - 1)] for _ in range(h)]
min_count = 4

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    mat[i - 1][j - 1] = 1
    
def down(line, mat):
    for dep in range(h):
        if line > 0 and mat[dep][line - 1]:
            line -= 1
        elif line < n - 1 and mat[dep][line]:
            line += 1
    return line

def check(mat):
    for i in range(n - 1):
        if down(i, mat) != i:
            return False
    return True

def dfs(count, mat, x, y):
    global min_count

    if count >= min_count:
        return 
    
    if count > 3:
        return 
    
    if check(mat):
        min_count = min(min_count, count)
        return
    
    for i in range(x, h):
        for j in range((y if i == x else 0), n - 1):
            if mat[i][j] == 0 and (j == 0 or mat[i][j - 1] == 0) and (j == n - 2 or mat[i][j + 1] == 0):
                mat[i][j] = 1
                dfs(count + 1, mat, i, j + 2)
                mat[i][j] = 0
    
for i in range(h):
    for j in range(n - 1):
        dfs(0, mat, i, j)

print(-1 if min_count > 3 else min_count)
