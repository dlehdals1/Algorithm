import math

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    count = 0
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            count = -1 
    else:
        if distance == r1 + r2:
            count = 1
        elif distance == abs(r1 - r2):
            count = 1 
        elif abs(r1 - r2) < distance < (r1 + r2):
            count = 2 
        else:
            count = 0
    print(count)
