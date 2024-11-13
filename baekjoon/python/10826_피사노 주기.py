n = int(input()) % (15 * 10 ** 5)
x1 = 0
x2 = 1
for i in range(n):
    temp = (x1 + x2) % 1000000
    x1 = x2
    x2 = temp
print(x1)