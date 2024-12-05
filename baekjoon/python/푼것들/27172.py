import sys

n = int(sys.stdin.readline())
num_org = list(map(int, sys.stdin.readline().split()))
num = sorted(num_org)
num_set = set(num)
score = [0] * (num[-1] + 1)

for i in num:
    for j in range(i * 2, num[-1] + 1, i):
        score[j] -= 1
        if j in num_set:
            score[i] += 1

for i in num_org:
    print(score[i], end = " ")