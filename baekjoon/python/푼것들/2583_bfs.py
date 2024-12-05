from collections import deque

def bfs(start_x, start_y, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y)])
    graph[start_x][start_y] = 1
    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    count += 1

    return count, graph


n ,m , k = map(int, input().split())
mat = [[0 for i in range(n)] for j in range(m)]
for i in range(k):
    ld_x, ld_y, ru_x, ru_y = map(int, input().split())
    for x in range(ld_x,ru_x):
        for y in range(ld_y, ru_y):
            mat[x][y] = 1

count = 0
size_list = []
for x in range(m):
    for y in range(n):
        if mat[x][y] == 0:
            count += 1
            size ,mat = bfs(x,y,mat)
            size_list.append(size)

size_list.sort()
print(count)
for size in size_list:
    print(str(size), end=" ")