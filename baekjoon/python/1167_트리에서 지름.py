import sys
from collections import  defaultdict
import sys

sys.setrecursionlimit(10**6)

v = int(sys.stdin.readline())
is_end = []
graph = defaultdict(list)
len_max = 0
visited = [0] * (v + 1)

for _ in range(v):
    nums = list(map(int, sys.stdin.readline().split()))
    start = nums[0]
    for i in range(1,len(nums),2):
        if nums[i] == -1:
            break
        graph[start].append([nums[i], nums[i + 1]])

for node in graph:
    if len(graph.get(node)) == 1:
        is_end.append(node)


end_1 = 0
def dfs(start, len):
    global len_max, end_1
    next_list = graph.get(start)
    for next_node in next_list:
        if visited[next_node[0]] == 0:
            visited[next_node[0]] = 1
            dfs(next_node[0], len + next_node[1])
            visited[next_node[0]] = 0
    if len > len_max:
        end_1 = start
        len_max = len
        
visited[1] = 1
dfs(1, 0)
visited[1] = 0

visited[end_1] = 1
dfs(end_1, 0)
visited[end_1] = 0

print(len_max)
