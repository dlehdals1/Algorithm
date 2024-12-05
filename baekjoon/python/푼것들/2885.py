import sys
k = int(sys.stdin.readline())
bin_k = str(bin(k))[2:]
d = len(bin_k)
n = 1
flag = True
for i in bin_k[::-1]:
    if i == "0" and flag:
        d -= 1
    else:
        flag = False
    n *= 2
if d == 1:
    d = 0
    n /= 2
print(int(n), d)