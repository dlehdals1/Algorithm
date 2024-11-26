import sys
from collections import deque
from queue import PriorityQueue
n, m, k = map(int, sys.stdin.readline().split())

nut = [[5 for _ in range(n)] for _ in range(n)]
trees = [[PriorityQueue() for _ in range(n)] for _ in range(n)]
dead = [[deque() for _ in range(n)] for _ in range(n)]

a = []

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x - 1][y - 1].put(z)


def spring():
    for i in range(n):
        for j in range(m):
            grow = PriorityQueue()    
            while trees[i][j]:
                youngest = trees[i][j].get()
                if nut[i][j] <= youngest:
                    nut[i][j] -= youngest
                    grow.put(youngest + 1)
                else:
                    dead[i][j].append(youngest)
            trees[i][j] = grow

def summer():
    for i in range(n):
        for j in range(m):   
            while dead[i][j]:
                nut[i][j] += dead[i][j].popleft() // 2

def autumn():
    for i in range(n):
        for j in range(m):
            bk = PriorityQueue()    
            while trees[i][j]:
                breed = trees[i][j].get()
                if breed % 5 == 0:
                    print()
                