import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
mat = [[float("inf") for _ in range(n)] for _ in range(n)]
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    start -= 1
    end -= 1
    mat[start][end] = cost
for i in range(n):
    mat[i][i] = 0
def dijkstra(start, end):
    for i in range(n):
        if mat[start][i] == float("inf"):
            continue
        
