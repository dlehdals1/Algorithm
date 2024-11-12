from collections import deque

n, m = map(int, input().split())
line = deque(range(1, n + 1))
pop_list = list(map(int, input().split()))
count = 0

for pop in pop_list:
    while line[0] != pop:
        idx = line.index(pop)
        if idx < len(line) - idx:
            line.rotate(-1)
            count += 1
        else:
            line.rotate(1)
            count += 1
    line.popleft()

print(count)
