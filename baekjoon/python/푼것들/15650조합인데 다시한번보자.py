import sys

n, m = map(int, sys.stdin.readline().split())

def dfs(i, list):
    if len(list) == m:
        print(*list, sep = " ")
        return
    
    for k in range(i, n):
        list.append(k + 1)
        dfs(k + 1, list)
        list.pop()
        # list = list[:-1]
        # 이거하면 새로운 리스트가 만들어져서 안됨

dfs(0, [])