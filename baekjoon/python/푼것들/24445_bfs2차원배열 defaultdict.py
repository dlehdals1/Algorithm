from collections import deque, defaultdict
import sys

n, m, r = map(int, sys.stdin.readline().split())
# mat = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
graph = defaultdict(list)
visited = [0 for _ in range(n + 1)]
v = [1 for _ in range(n + 1)]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    # mat[i][j] = 1
    # mat[j][i] = 1
    graph[i].append(j)
    graph[j].append(i)

for i in graph:
    graph[i].sort(reverse=True)

def bfs(start):
    count = 0
    queue = deque([start])
    
    while queue:
        count += 1
        temp = queue.popleft()
        visited[temp] = count
        v[temp] = 0
        insert_list = []
        # for i in range(n + 1):
        for i in graph[temp]:
            if v[i]:
                v[i] = 0
                insert_list.append(i)
        queue += insert_list 

bfs(r)

for i in range(1, n + 1):
    print(visited[i])