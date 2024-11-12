def command_move(dice, x, y, mat, command):
    new_x = x
    new_y = y
    if command == 1:
        if y == len(mat[0]) - 1:
            return dice, mat, x, y , False
        temp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = temp
        new_x = x 
        new_y = y + 1

    elif command == 2:
        if y == 0:
            return dice, mat, x, y , False
        temp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = temp
        new_x = x
        new_y = y - 1

    elif command == 3:
        if x == 0:
            return dice, mat, x, y , False
        temp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = temp
        new_x = x - 1
        new_y = y 
        
    elif command == 4:
        if x == len(mat) - 1:
            return dice, mat, x, y , False
        temp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = temp
        new_x = x + 1
        new_y = y

    if mat[new_x][new_y] == 0:
        mat[new_x][new_y] = dice[6]
    else:
        dice[6] = mat[new_x][new_y]
        mat[new_x][new_y] = 0
    
    return dice, mat, new_x, new_y, True
    

dice = [0 for i in range(7)]

n, m, x, y, k = map(int, input().split())

mat = []

for i in range(n):
    mat.append(list(map(int, input().split())))

commands = (list(map(int, input().split())))

for command in commands:
    dice, mat, x, y, moved = command_move(dice, x, y, mat, command)
    if moved:
        print(dice[1])
    # print()
    # print(command)
    # print(dice)
    # for i in mat:
    #     print(i[0], i[1])