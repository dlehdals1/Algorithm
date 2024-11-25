import sys
from collections import  deque

n, m = map(int, sys.stdin.readline().split())
mat = []
start = (0, 0)
goal = (n -1, m - 1)

for _ in range(n):
    mat.append(list(map(int, (list(sys.stdin.readline().strip())))))

def brake(i, j):
    acts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    count = 0
    for act in acts:
        ni, nj = i + act[0], j + act[1]
        if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 0:
            count += 1
    return count >= 2


brake_list = []

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and brake(i, j):
            brake_list.append((i, j))


def bfs():
    acts = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([(0, 0, 1, False)])
    visited = set()
    visited.add((0, 0, False))

    while q:
        x, y ,count, broke = q.popleft()
        if (x, y) == goal:
            return count
        
        for act in acts:
            next_pos = (x + act[0], y + act[1])
            if 0 <= next_pos[0] < n and 0 <= next_pos[1] < m:

                if mat[next_pos[0]][next_pos[1]] == 0 and (next_pos[0], next_pos[1], broke) not in visited:
                    q.append((next_pos[0], next_pos[1], count + 1, broke))
                    visited.add((next_pos[0], next_pos[1], broke))
                    
                if mat[next_pos[0]][next_pos[1]] == 1 and (next_pos[0], next_pos[1], True) not in visited and not broke:
                    q.append((next_pos[0], next_pos[1], count + 1, True))
                    visited.add((next_pos[0], next_pos[1], True))
                    
    return -1

print(bfs())