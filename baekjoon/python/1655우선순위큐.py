import sys
from queue import PriorityQueue

small = PriorityQueue()
big = PriorityQueue()
n = int(sys.stdin.readline())

for i in range(n):
    k = int(sys.stdin.readline())
    
    if small.qsize() == 0 :
        small.put(-1 * k)
        print(k)
        continue

    big_size = big.qsize()
    small_size = small.qsize()

    mid = small.queue[0] * -1
    if big_size > 0:
        big_mid = big.queue[0]
    else:
        big_mid = 10001

    if big_size == small_size:
        if big_mid >= k:
            small.put(k * -1)
        else:
            small.put(big.get() * -1)
            big.put(k)
    else:
        if mid <= k:
            big.put(k)
        else:   
            big.put(small.get() * -1)
            small.put(k * -1)
            
    print(small.queue[0] * -1)