import sys

def bingos(O_count, X_count):
    count = 0
    bingo = "None"
    for OX in [O_count, X_count]:
        if 1 in OX and 2 in OX and 3 in OX:
            count += 1
        if 4 in OX and 5 in OX and 6 in OX:
            count += 1
        if 7 in OX and 8 in OX and 9 in OX:
            count += 1
        if 1 in OX and 4 in OX and 7 in OX:
            count += 1
        if 2 in OX and 5 in OX and 8 in OX:
            count += 1
        if 3 in OX and 6 in OX and 9 in OX:
            count += 1
        if 1 in OX and 5 in OX and 9 in OX:
            count += 1
        if 3 in OX and 5 in OX and 7 in OX:
            count += 1
        if count > 1:
            return "over"
        if count:
            if OX == O_count:
                bingo = "O"
            else:
                bingo = "X"
    return bingo
        

while True:
    O_count = set()
    X_count = set()

    mat = sys.stdin.readline().strip()
    
    if mat == 'end':
        break
    
    for i in range(9):
        if mat[i] == "O":
            O_count.add(i + 1)
        elif mat[i] == "X":
            X_count.add(i + 1)

    
    if len(O_count) == len(X_count) or len(O_count) == len(X_count) - 1:

        result = bingos(O_count, X_count)

        print(result)
        print(O_count, X_count)

        if result == "O" and len(O_count) != len(X_count):
            print("invalid")
            continue

        if result == "X" and len(O_count) != len(X_count) - 1:
            print("invalid")
            continue
        
        if result == "None" and (len(X_count) != 5 or len(O_count) != 4):
            print("invalid")
            continue
        
    else:
        print("invalid")
        continue

    print("valid")