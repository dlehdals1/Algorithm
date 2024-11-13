import sys
n = int(sys.stdin.readline())
a = "ABCDEFGHIJKL"
print(a[(n + 8) % 12] + str((n + 6) % 10))