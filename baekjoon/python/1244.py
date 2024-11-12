def rev(switch_list,num):
    switch_list[num] = 1 - switch_list[num]

def boy(switch_list,num,length):
    temp = num
    while temp <= length:
        rev(switch_list,temp)
        temp += num
        
def girl(switch_list,num,length):
    i = 1
    rev(switch_list,num)
    while num + i <= length and num - i > 0 and switch_list[num + i] == switch_list[num - i]:
        rev(switch_list,num + i)
        rev(switch_list,num - i)
        i += 1


length = int(input())
switch_list = [-1] + list(map(int, input().split()))
t = int(input())
for i in range(t):
    gender, num = map(int, input().split())
    if gender == 1:
        boy(switch_list,num,length)
    else:
        girl(switch_list,num,length)
for i in range(1, length + 1):
    print(switch_list[i], end=" ")
    if i % 20 == 0:
        print()
