import sys

n = int(sys.stdin.readline())

for _ in range(n):
    str = sys.stdin.readline().strip()
    rev = str[::-1]
    new_str = str
    lenght = len(str)
    i = lenght
    while not (new_str[:lenght] == str and (new_str[::-1])[0:lenght] == str):
        new_str = str + rev[i:lenght] 
        i -= 1
    print(new_str)