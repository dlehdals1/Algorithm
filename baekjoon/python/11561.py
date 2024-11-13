import sys
import math
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    m = int(math.sqrt(2 * n))
    for i in range(m - 2,m + 3):
        if i**2 + i <= 2 * n < i**2 + 3*i + 2:
            print(i)
            break