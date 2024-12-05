import sys

n, m = map(int, sys.stdin.readline().split())
array = list(range(m + 1))

for i in range(2, m + 1):
    for j in range(2 * i, m + 1, i):
        array[j] = 0

for i in range(n, m + 1):
    if array[i] != 0 and array[i] != 1:
        print(array[i])