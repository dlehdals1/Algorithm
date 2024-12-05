from collections import deque

def bfs(start, mat,under_count):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    time = 0
    start_time_que = deque([])
    start_time_que.append(start)

    while start_time_que:
        new_que = deque([])
        queue = start_time_que.popleft()
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < len(mat) and 0 <= ny < len(mat[0]):
                    if mat[nx][ny] == 0:
                        mat[nx][ny] = 1
                        under_count -= 1
                        new_que.append((nx, ny))
        if new_que:
            start_time_que.append(new_que)
        time += 1
    return time, under_count

line = list(map(int, input().split()))
m = int(line[0])
n = int(line[1])
mat = [[0 for i in range(m)] for j in range(n)]

under_count = 0
start = deque([])
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        mat[i][j] = line[j]
        if mat[i][j] == 1:
            start.append((i,j))
        elif mat[i][j] == 0:
            under_count += 1

time, under_count = bfs(start, mat, under_count)

if under_count != 0:
    print(-1)
else:
    print(time - 1)