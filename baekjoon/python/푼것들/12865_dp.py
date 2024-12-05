n, k = map(int, input().split())
bag = []
for i in range(n):
    weight, value = map(int, input().split())
    bag.append((weight, value))

dp = [0] * (k + 1)

for weight, value in bag:
    for i in range(k, weight - 1, -1):
        dp[i] = max(dp[i], dp[i - weight] + value)

print(dp[k])
