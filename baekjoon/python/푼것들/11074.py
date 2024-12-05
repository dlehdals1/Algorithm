import sys

n, r, c = map(int, sys.stdin.readline().split())
count = 0
while n > 0:
    half = pow(2, n-1)
    if r >= half:
        r -= half
        if c >= half:
            c -= half
            count += half * half * 3
        else:
            count += half * half * 2
    else:
        if c >= half:
            c -= half
            count += half * half * 1
        else:
            count += half * half * 0
    n -= 1
print(count)