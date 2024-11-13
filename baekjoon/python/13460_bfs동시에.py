from collections import deque

n, m = map(int, input().split())
mat = []

for i in  range(n):
    mat.append(list(input()))
    for j in range(m):
        if mat[i][j] == 'R':
            rx, ry = i, j
        elif mat[i][j] == 'B':
            bx, by = i, j


def bfs(rx, ry, bx, by, mat):
    acts = [(1,0),(-1,0),(0,1),(0,-1)]
    count = 0
    q = deque([(rx, ry, bx, by)])
    visited = set([(rx, ry, bx, by)])
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10:
                return -1
            if mat[rx][ry] == "O":
                return count
            for act in acts:
                nrx, nry, nbx, nby = rx, ry, bx, by
                while mat[nrx + act[0]][nry + act[1]] != "#" and mat[nrx][nry] != "O":
                    nrx += act[0]
                    nry += act[1]
                while mat[nbx + act[0]][nby + act[1]] != "#" and mat[nbx][nby] != "O":
                    nbx += act[0]
                    nby += act[1]
                if mat[nbx][nby] == "O":
                    continue
                if nrx == nbx and nry == nby:
                    if abs(rx - nrx) + abs(ry - nry) > abs(bx - nbx) + abs(by - nby):
                        nrx -= act[0]
                        nry -= act[1]
                    else:
                        nbx -= act[0]
                        nby -= act[1]
                if (nrx, nry, nbx, nby) not in visited:
                    visited.add((nrx, nry, nbx, nby))
                    q.append((nrx, nry, nbx, nby))
        count += 1
    return -1
print(bfs(rx, ry, bx, by, mat))