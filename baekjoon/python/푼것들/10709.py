import sys
h, w = map(int, sys.stdin.readline().split())
result = [[-1 for _ in range(w)] for _ in range(h)]
clouds = []

def weather_to_num(weather):
    if weather == "c":
        return 0
    if weather == ".":
        return -1

for i in range(h):
    weather_line = list(sys.stdin.readline().strip())
    for j,weather in enumerate(weather_line):
        if weather == "c":
            result[i][j] = 0
            clouds.append([i, j])

for time in range(1, w):
    for cloud in clouds:
        new_cloud = cloud[1] + time
        if new_cloud >= w:
            continue
        if result[cloud[0]][new_cloud] == -1:
            result[cloud[0]][new_cloud] = time
for i in range(h):
    print(*result[i], sep=" ")