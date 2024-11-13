def max_before(connect, target, time, time_memory):
    if time_memory[target] != -1:
        return time_memory[target]
    
    if not connect[target]: 
        time_memory[target] = int(time[target - 1])
        return time_memory[target]
    
    before_time = []
    for i in connect[target]:
        before_time.append(max_before(connect, i, time, time_memory))
    
    time_memory[target] = max(before_time) + int(time[target - 1])
    return time_memory[target]


count = int(input())
for _ in range(count):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    connect = [[] for _ in range(n + 1)]
    time_memory = [-1 for _ in range(n + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        connect[y].append(x)
    target = int(input())
    print(max_before(connect, target, time, time_memory))
