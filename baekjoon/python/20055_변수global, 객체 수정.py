import sys

n, k = map(int, sys.stdin.readline().split())
durability = list(map(int, sys.stdin.readline().split()))
is_robot = [0] * 2 * n
count_0_dur = 0
step = 0
on = 0
off = n - 1
robots = []

def next_step():
    global on, off
    on = (on - 1) % (2 * n)
    off = (off - 1) % (2 * n)
    i = 0
    while i < len(robots):
        if robots[i] == off:
            is_robot[robots[i]] = 0
            del robots[i]
        else:
            i += 1

def robot_move():
    global count_0_dur
    i = 0
    while i < len(robots):
        next_step = (robots[i] + 1) % (2 * n)
        if durability[next_step] > 0 and is_robot[next_step] == 0:
            is_robot[robots[i]] = 0
            is_robot[next_step] = 1
            robots[i] = next_step
            durability[next_step] -= 1
            if durability[next_step] == 0:
                count_0_dur += 1
        if robots[i] == off:
            is_robot[robots[i]] = 0
            del robots[i]
        else:
            i += 1
        
def put_on_robot():
    global count_0_dur
    if durability[on] > 0 and is_robot[on] == 0:
        durability[on] -= 1
        if durability[on] == 0:
                count_0_dur += 1
        is_robot[on] = 1
        robots.append(on)


while count_0_dur < k:
    next_step()
    robot_move()
    put_on_robot()
    step += 1
print(step)

# is_robot[robots[i]] = 0 같은 경우에는 리스트의 특정 인덱스에 값을 대입하는 것이기 때문에 문제가 발생하지 않습니다. 
# 이는 Python에서 로컬 변수로 처리되는 것이 아니라, 리스트 객체 내부의 데이터를 수정하는 작업이기 때문입니다.

# 중요한 차이점: 변수 대입 vs. 객체 수정
#     변수 대입 (on = ...)
#         on = (on - 1) % (2 * n)와 같은 코드는 변수 on에 새로운 값을 대입하는 것입니다. 
#         Python은 이 순간 on을 로컬 변수로 간주하고, 함수 내부에 on이 초기화되지 않은 상태에서 사용하려고 하면 UnboundLocalError가 발생합니다.

# 객체 수정 (is_robot[robots[i]] = 0)
#     is_robot는 리스트 객체입니다. 
#         is_robot[robots[i]] = 0는 리스트 is_robot의 특정 인덱스에 있는 값을 수정하는 작업입니다. 
#         리스트는 가변 객체이므로, 함수 내부에서 수정하더라도 글로벌 스코프의 리스트에 영향을 미칩니다. 따라서 Python은 이것을 로컬 변수로 간주하지 않으며, 에러가 발생하지 않습니다.