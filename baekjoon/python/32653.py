import math
import sys

n = int(sys.stdin.readline())
x_time = list(map(int, sys.stdin.readline().split()))
time = 1

print(2 * math.lcm(*x_time))