from collections import deque

def bfs(start_x, start_y, graph, color):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(start_x, start_y)])
    graph[start_x][start_y] = 0
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == color:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))

    return graph

def color_to_num(color):
    if color == "R":
        return 1
    elif color == "G":
        return 2
    elif color == "B":
        return 3

def color_to_num_RG(color):
    if color == "B":
        return 3
    else:
        return 1    

n = int(input())
mat = []
mat_RG = []
for i in range(n):
    color_line = list(input())
    num_line = []
    num_line_RG = []
    for color in color_line:
        num_line.append(color_to_num(color))
        num_line_RG.append(color_to_num_RG(color))
    mat.append(num_line)
    mat_RG.append(num_line_RG)

count = 0
count_RG = 0

for x in range(len(mat)):
    for y in range(len(mat[0])):
        if mat[x][y] != 0:
            count += 1
            mat = bfs(x,y,mat,mat[x][y])
        if mat_RG[x][y] != 0:
            count_RG += 1
            mat_RG = bfs(x,y,mat_RG,mat_RG[x][y])
        

print(count, count_RG)
