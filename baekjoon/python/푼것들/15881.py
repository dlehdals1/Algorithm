import sys

n = int(sys.stdin.readline())
str = sys.stdin.readline()
count = 0
i = 0
while i < n:
    if i + 4 <= n and str[i : i + 4] == "pPAp":
        count += 1
        i += 4
    else:
        i += 1
print(count)