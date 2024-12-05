import sys

n = int(sys.stdin.readline())
mat = []
food = set()
shark = 2
move_count = 0


# 굳이 안해도 될듯?
def smaller_food_exist():
    for i in range(1, shark):
        # set 타입 검색
        # [item for item in food if item[2] == i]
        # next((item for item in food if item[2] == i), None)
        if any(k == i for _, _, k in food): 
            return True
        
    return False

for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))
    for j in range(n):
        if mat[i][j] == 0:
           continue
        if mat[i][j] == 9:
            start = [i , j]
        else:
            food.add((i , j, mat[i][j]))

while smaller_food_exist():
    
print(move_count)