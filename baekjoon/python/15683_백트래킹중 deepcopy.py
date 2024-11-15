import sys
from collections import deque
import copy

n, m = map(int, sys.stdin.readline().split())
cctv_mat = []
cctv = deque()

for i in range(n):
    cctv_mat.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if 0 < cctv_mat[i][j] < 6:
            cctv.append([i, j, cctv_mat[i][j]])

def count_blind(mat):
    count = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                count += 1
    return count

def look1(x,y,mat):
    nx = x - 1
    while nx > -1 and mat[nx][y] != 6:
        if mat[nx][y] == 0:
            mat[nx][y] = "#"
        nx -= 1

def look2(x,y,mat):
    nx = x + 1
    while nx < n and mat[nx][y] != 6:
        if mat[nx][y] == 0:
            mat[nx][y] = "#"
        nx += 1

def look3(x,y,mat):
    ny = y - 1
    while ny > -1 and mat[x][ny] != 6:
        if mat[x][ny] == 0:
            mat[x][ny] = "#"
        ny -= 1

def look4(x,y,mat):
    ny = y + 1
    while ny < m and mat[x][ny] != 6:
        if mat[x][ny] == 0:
            mat[x][ny] = "#"
        ny += 1

def look_dir(x, y, kind, diretcion, new_mat):
    if kind == 1:
        if diretcion == 1:
            look1(x,y,new_mat)
        elif diretcion == 2:
            look2(x,y,new_mat)
        elif diretcion == 3:
            look3(x,y,new_mat)
        elif diretcion == 4:
            look4(x,y,new_mat)
    elif kind == 2:
        if diretcion == 1:
            look1(x,y,new_mat)
            look2(x,y,new_mat)
        elif diretcion == 2:
            look3(x,y,new_mat)
            look4(x,y,new_mat)
    elif kind == 3:
        if diretcion == 1:
            look1(x,y,new_mat)
            look3(x,y,new_mat)
        elif diretcion == 2:
            look1(x,y,new_mat)
            look4(x,y,new_mat)
        elif diretcion == 3:
            look2(x,y,new_mat)
            look3(x,y,new_mat)
        elif diretcion == 4:
            look2(x,y,new_mat)
            look4(x,y,new_mat)
    elif kind == 4:
        if diretcion == 1:
            look1(x,y,new_mat)
            look2(x,y,new_mat)
            look3(x,y,new_mat)
        elif diretcion == 2:
            look2(x,y,new_mat)
            look3(x,y,new_mat)
            look4(x,y,new_mat)
        elif diretcion == 3:
            look3(x,y,new_mat)
            look4(x,y,new_mat)
            look1(x,y,new_mat)
        elif diretcion == 4:
            look4(x,y,new_mat)
            look1(x,y,new_mat)
            look2(x,y,new_mat)
    elif kind == 5:
        look1(x,y,new_mat)
        look2(x,y,new_mat)
        look3(x,y,new_mat)
        look4(x,y,new_mat)

def dfs(depth, mat):
    if depth == len(cctv):
        return count_blind(mat)
    
    x, y, kind = cctv[depth]
    min_blind = 100

    directions = []
    if kind == 1:
        directions = [1, 2, 3, 4]
    elif kind == 2:
        directions = [1, 2]
    elif kind == 3:
        directions = [1, 2, 3, 4]
    elif kind == 4:
        directions = [1, 2, 3, 4]
    elif kind == 5:
        directions = [1]
    
    for dir in directions:
        new_mat = copy.deepcopy(mat)

        look_dir(x, y, kind, dir, new_mat)

        min_blind = min(min_blind, dfs(depth + 1, new_mat))
        

    return min_blind

print(dfs(0, cctv_mat))
