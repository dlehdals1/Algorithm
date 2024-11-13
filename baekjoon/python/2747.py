n = int(input())
x1 = 0
x2 = 1
for i in range(n):
    temp = x1 + x2
    x1 = x2
    x2 = temp
print(x1)