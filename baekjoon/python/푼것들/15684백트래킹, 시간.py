import sys

n, m, h = map(int, sys.stdin.readline().split())
mat = [[0 for _ in range(n - 1)] for _ in range(h)]
min_count = 4

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    mat[i - 1][j - 1] = 1
    

def check(mat):
    for i in range(n - 1):
        temp = i
        for j in range(h):
            if temp > 0 and mat[j][temp - 1] == 1:
                temp -= 1
            elif temp < n - 1 and mat[j][temp] == 1:
                temp += 1
            else:
                continue
        if i != temp:
            return False
    return True

def dfs(count, mat, x, y):
    global min_count

    if count >= min_count:
        return 
    
    if check(mat):
        min_count = min(min_count, count)
        return
    
    if count == 3:
        return 
    
    for i in range(x, h):
        for j in range((y if i == x else 0), n - 1):
            # if mat[i][j] == 0 and (j > 0 or mat[i][j - 1] == 1) and (j == n - 2 or mat[i][j + 1] == 0):
            if mat[i][j] == 0:
                if j > 0 and mat[i][j - 1] == 1:
                    continue
                if j < n - 2 and mat[i][j + 1] == 1:
                    continue
                mat[i][j] = 1
                dfs(count + 1, mat, i, j + 2)
                mat[i][j] = 0
    
dfs(0, mat, 0, 0)

print(-1 if min_count > 3 else min_count)
