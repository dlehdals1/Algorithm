import sys

n, m = map(int, sys.stdin.readline().split())
mat = []
chicken = []
home = []
city_chick_dist = float("inf")

for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if mat[i][j] == 1:
            home.append((i,j))
        if mat[i][j] == 2:
            chicken.append((i,j))

count_chick = len(chicken)

def dis_add(home_list, chick_list):
    s = 0
    for x in home_list:
        smallest = float("inf")
        for y in chick_list:
            smallest = min(smallest, abs(x[0] - y[0]) + abs(x[1] - y[1]))
        s += smallest
    return s

def dfs(count, chick_list, idx):
    global city_chick_dist
    # 더 좋은 조건이 뒤에 있다면 찾지 못할 가능성이 잇음
    # if dis_add(home, chick_list) > city_chick_dist:
    #     return
    
    if count == m:
        city_chick_dist = min(city_chick_dist, dis_add(home, chick_list))
        return
    
    for i in range(idx, count_chick):
        dfs(count + 1, chick_list + [chicken[i]], i + 1)

dfs(0,[],0)
print(city_chick_dist)