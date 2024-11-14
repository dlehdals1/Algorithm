import sys

n, m = map(int, sys.stdin.readline().split())
s = []
visited = [0] * (n + 1)

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = 1
        s.append(i)
        dfs()
        s.pop()
        visited[i] = 0
dfs()