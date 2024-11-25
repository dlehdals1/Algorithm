import sys

n = int(sys.stdin.readline())
day_pay = []
dp = [0] * n
max_pay = 0

for _ in range(n):
    day_pay.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    max_pay = max(dp[i], max_pay)
    dp[i] = max_pay 
    if day_pay[i][0] + i - 1 < n:
        dp[day_pay[i][0] + i - 1] = max(dp[day_pay[i][0] + i - 1], dp[i - 1] + day_pay[i][1])
    max_pay = max(dp[i], max_pay)

print(max_pay)