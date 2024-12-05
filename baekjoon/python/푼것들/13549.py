import sys

n, m = map(int, sys.stdin.readline().split())

dp = [float("inf")] * 200000

for i in range(n + 1):
    dp[i] = n - i
    if 2 * i > n and 2 * i < len(dp):
        dp[2 * i] = n - i


if m <= n:
    print(dp[m])
else:
    for i in range(n + 1, m + 1):
        if i % 2 == 0:
            dp[i] = min(dp[i - 1] + 1, dp[i + 1] + 1, dp[i // 2])
        if i % 2 == 1:
            dp[i] = min(dp[i - 1] + 1, dp[i + 1] + 1)
        if 2 * i < len(dp):
            dp[2 * i] = min(dp[2 * i], dp[i])

    print(dp[m])