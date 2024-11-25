import sys
import queue

n = int(sys.stdin.readline())
str = list(sys.stdin.readline().strip())
B_list = [0]
O_list = []
J_list = []

dp = [0] * n

for i in range(1,n):
    able_list = queue.PriorityQueue()
    if str[i] == "B" and J_list:
        B_list.append(i)
        for j in J_list:
            able_list.put(dp[j] + (i - j) ** 2 )
    if str[i] == "O" and B_list:
        O_list.append(i)
        for j in B_list:
            able_list.put(dp[j] + (i - j) ** 2 )
        
    if str[i] == "J" and O_list:
        J_list.append(i)
        for j in O_list:
            able_list.put(dp[j] + (i - j) ** 2 )

    if not able_list.empty():
        dp[i] = (able_list.get())
    else:
        dp[i] = -1

print(dp[i])    