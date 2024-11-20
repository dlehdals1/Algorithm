import sys

n, k = map(int, sys.stdin.readline().split())
classrooms = [0] + list(map(int, sys.stdin.readline().split()))
dis = []
classrooms.sort()

for i in range(n):
    dis.append(classrooms[i + 1] - classrooms[i])

dis.sort(reverse=True)
dis_sum = 0
for i in dis:
    if k > 0:
        k -= 1
        continue
    dis_sum += i
print(dis_sum)