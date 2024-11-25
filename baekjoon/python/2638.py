import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
mat = []
cheese = []

def bfs():
    global visited
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]) and (nx, ny) not in visited and mat[nx][ny] == 0:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return 

for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if mat[i][j]:
            cheese.append([i, j])

time = 0

while len(cheese):
    visited = set()
    bfs()

    melt = []
    new_cheese = []
    for c in cheese:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        count = 0
        for i in range(4):
            nx = c[0] + dx[i]
            ny = c[1] + dy[i]

            if (nx, ny) in visited:
                count += 1
        if count >= 2:
            mat[c[0]][c[1]] = 0
        else:
            new_cheese.append([c[0], c[1]])
    cheese = new_cheese
    time += 1
print(time)