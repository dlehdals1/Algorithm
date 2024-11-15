import sys

n, k = map(int, sys.stdin.readline().split())
durability = list[map(int, sys.stdin.readline().split())]
is_robot = [0] * 2 * n
count_0_dur = 0
step = 0
on = 0
off = n - 1
robots = []

def robot_move():
    for i in range(robots):
        next_step = (robots[i] + 1) % (2 * n)
        if durability[next_step] > 0 and is_robot[next_step] == 0:
            is_robot[robots[i]] = 0
            is_robot[next_step] = 1
            robots[i] = next_step
            durability[next_step] -= 1

        if robots[i] == off:
            is_robot[robots[i]] = 0
            del robots[i]
        

def next_step():
    step += 1
    on = (on - 1) % (2 * n)
    off = (off - 1) % (2 * n)
    for i in range(robots):
        if robots[i] == off:
            is_robot[robots[i]] = 0
            del robots[i]


while count_0_dur < k:
            


