from collections import deque

n = int(input())
k = int(input())

map = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
for i in range(n+2):
    map[0][i] = -1
    map[n+1][i] = -1
    map[i][0] = -1
    map[i][n+1] = -1
    
for _ in range(k):
    x_y = input()
    map[int(x_y.split(" ")[0])][int(x_y.split(" ")[1])] = 1


time_rule = deque() 
dir_rule = deque()

l = int(input())

for _ in range(l):
    rule = input()
    time_rule.append(int(rule.split(" ")[0]))
    if rule.split(" ")[1] == "L":
        dir_rule.append(3)
    if rule.split(" ")[1] == "D":
        dir_rule.append(1)
    

count = 0
snake = deque([[1,1]])
dir = 0
cur_time_rule = time_rule.popleft() if time_rule else None
cur_dir_rule = dir_rule.popleft() if dir_rule else None


while 1:
    count += 1
    snake_head = snake[-1]
    if dir == 0:
        snake.append([snake_head[0], snake_head[1] + 1])
    if dir == 1:
        snake.append([snake_head[0] + 1, snake_head[1]])
    if dir == 2:
        snake.append([snake_head[0], snake_head[1] - 1])
    if dir == 3:
        snake.append([snake_head[0] - 1, snake_head[1]])

    snake_head = snake[-1]

    if map[snake_head[0]][snake_head[1]] == -1 or snake_head in list(snake)[:-1]:
        break
    
    if map[snake_head[0]][snake_head[1]] == 0:
        snake.popleft()
    elif map[snake_head[0]][snake_head[1]] == 1:
        map[snake_head[0]][snake_head[1]] = 0


    if count == cur_time_rule:
        dir = (dir + cur_dir_rule) % 4
        cur_time_rule = time_rule.popleft() if time_rule else None
        cur_dir_rule = dir_rule.popleft() if dir_rule else None

print(count)

