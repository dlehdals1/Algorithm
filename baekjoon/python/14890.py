import sys

n, l = map(int, sys.stdin.readline().split())
mat = []
is_flatx = [[0 for _ in range(n)] for _ in range(n)]
is_flaty = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

def lookback(i, j):
    if j >= l :
        for k in range(j - l,j):
            if mat[i][k] != mat[i][j - 1] or is_flatx[i][k] != 0:
                return 0
            is_flatx[i][k] = 1
        return 1
    else:
        return 0
    
def lookforward(i, j):
    if n - j + 1 > l :
        for k in range(j, j + l):
            if mat[i][k] != mat[i][j] or is_flatx[i][k] != 0:
                return 0
            is_flatx[i][k] = 1
        return 1
    else:
        return 0
  
def lookbacky(j, i):
    if j >= l :
        for k in range(j - l,j):
            if mat[k][i] != mat[j - 1][i] or is_flaty[k][i] != 0:
                return 0
            is_flaty[k][i] = 1
        return 1
    else:
        return 0
    
def lookforwardy(j, i):
    if n - j + 1 > l :
        for k in range(j, j + l):
            if mat[k][i] != mat[j][i] or is_flaty[k][i] != 0:
                return 0
            is_flaty[k][i] = 1
        return 1
    else:
        return 0
    

count = 0
for i in range(n):
    before = 0
    add_count = 1
    for j in range(n):
        now = mat[i][j]
        if now == before or before == 0:
            before = now
            continue
        elif now - before == 1:
            add_count = lookback(i,j)
        elif before - now == 1:
            add_count = lookforward(i,j)
        else:
            add_count = 0
        if add_count == 0:
            break
        before = now
    count += add_count

    before = 0
    add_count = 1
    for j in range(n):
        now = mat[j][i]
        if now == before or before == 0:
            before = now
            continue
        elif now - before == 1:
            add_count = lookbacky(j,i)
        elif before - now == 1:
            add_count = lookforwardy(j,i)
        else:
            add_count = 0
        if add_count == 0:
            break
        before = now
    count += add_count


print(count)