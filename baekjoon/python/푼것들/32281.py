import sys

n = int(sys.stdin.readline())
str = sys.stdin.readline()
con = []
flag = False
count = 0
for i in range(n):
    
    if str[i] == "0":
        flag = False

    if str[i] == "1":
        flag = True
    
    if flag:
        count += 1
    else:
        if count != 0:
            con.append(count)
        count = 0
if count != 0:
    con.append(count)
sum = 0
for i in con:
    sum += i * (i + 1) / 2
print(int(sum))