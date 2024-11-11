      
stair=[0]
n = int(input())
for i in range(1,n + 1):
    stair.append(int(input()))
sum = [[0 for i in range(n + 1)] for j in range(2)]
sum[0][0] = 0
sum[1][0] = 0
sum[0][1] = stair[1]
sum[1][1] = stair[1]
for i in range(2,n + 1):
    sum[1][i] = max(sum[0][i - 1], sum[1][i - 2]) + stair[i]
    sum[0][i] = sum[1][i-2] + stair[i]
    
print(max(sum[1][n],sum[0][n]))