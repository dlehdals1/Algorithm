import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())

def bfs(start, end, up, down):
    q = deque([[start , 0]])
    visited = set()
    while q:
        now = q.popleft()
        if now[0] == end:
            print(now[1])
            return
        else:
            nu = now[0] + up
            nd = now[0] - down
            if nu not in visited and 0 < nu <= f:
                visited.add(nu)
                q.append([nu, now[1] + 1])
            if nd not in visited and 0 < nd <= f:
                visited.add(nd)
                q.append([nd, now[1] + 1])
    print("use the stairs")

bfs(s, g, u, d)