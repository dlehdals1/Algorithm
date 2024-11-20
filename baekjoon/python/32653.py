import sys

n = int(sys.stdin.readline())
x_time = list(map(int, sys.stdin.readline().split()))
time = 1

def min_com_mul(a, b):
    list_a = []
    list_b = []

    for i in range(1, b + 1):
        list_a.append(i * a)

    for i in range(1, a + 1):
        list_b.append(i * b)

    for i in list_a:
        if i in list_b:
            return i

for x in x_time:
    time = min_com_mul(time, x)
print(2 * time)