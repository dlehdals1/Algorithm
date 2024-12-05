
n = int(input())
upper = list(map(int, input().split()))
lower = list(map(int, input().split()))
height = [0]*n
for i in range(n):
    height[i] = upper[i] - lower[i]
q = int(input())
temp = list(map(int, input().split()))
birds = []
for idx, t in enumerate(temp):
    birds.append((t,idx))
birds.sort(key = lambda x : -x[0])
current = 0
results = [0]*q
for i in range(q):
    size, idx = birds[i]
    while current < n and height[current] >= size:
        current += 1
    results[idx] = current

print(*results, sep='\n')