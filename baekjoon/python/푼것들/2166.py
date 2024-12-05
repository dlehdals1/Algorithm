import sys

n = int(sys.stdin.readline())
ver = []

for _ in range(n):
    ver.append(tuple(map(int, sys.stdin.readline().split())))
ver.append(ver[0])
area = 0

for i in range(n):
    area += ver[i][0] * ver[i + 1][1] - ver[i + 1][0] * ver[i][1]


print(abs(area) / 2)
