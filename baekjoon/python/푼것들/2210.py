import sys
mat = []
num_set = set()
for _ in range(5):
    mat.append(input().split())

def dfs(x, y, num):
    if len(num) == 6: 
        num_set.add(num)
        return

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, num + mat[nx][ny])

for i in range(5):
    for j in range(5):
        dfs(i, j, "")

print(len(num_set))