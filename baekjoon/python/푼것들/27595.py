import sys
from queue import PriorityQueue

q = PriorityQueue()

x = sys.stdin.read().splitlines()

flag = True

for f in x:
    for j in f.split():
        if flag:
            flag = False
            continue
        add = int(j[::-1])
        if add != 0:
            q.put(add)

while not q.empty():
    print(q.get()) 