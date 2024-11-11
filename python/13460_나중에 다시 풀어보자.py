from collections import deque

line = input()

n = int(line.split(" ")[0])
m = int(line.split(" ")[1])


map = [["#" for _ in range(m)] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

bfs_list = deque()

for i in range(n):
    line = list(input())
    for j in range(m):
        map[i][j] = line[j]
        
        if map[i][j] == "#":
            visited[i][j] = 1
        
        if map[i][j] == "R":
            red = [i,j]

        if map[i][j] == "B":
            blue = [i,j]

        if map[i][j] == "O":
            whole = [i,j]

