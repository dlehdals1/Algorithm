import sys
mat = []

for _ in range(10):
    mat.append(list(sys.stdin.readline().strip()))
def check_col(i,j):
    add1 = 0
    add2 = 0
    while j - add1 > -1 and mat[i][j - add1] =="X":
        add1 += 1
    while j + add2 < 10 and mat[i][j + add2] =="X":
        add2 +=1
    return -1 + add1 + add2

def check_row(i,j):
    add1 = 0
    add2 = 0
    while i - add1 > -1 and mat[i - add1][j] =="X":
        add1 += 1
    while i + add2 < 10 and mat[i + add2][j] =="X":
        add2 +=1
    return -1 + add1 + add2


def check_diagona1(i,j):
    add1 = 0
    add2 = 0
    while i - add1 > -1 and j - add1 > -1 and mat[i - add1][j - add1] =="X":
        add1 += 1
    while i + add2 < 10 and j + add2 < 10 and mat[i + add2][j + add2] =="X":
        add2 +=1
    return -1 + add1 + add2


def check_diagona2(i,j):
    add1 = 0
    add2 = 0
    while i - add1 > -1 and j + add1 < 10 and mat[i - add1][j + add1] =="X":
        add1 += 1
    while i + add2 < 10 and j - add2 > -1 and mat[i + add2][j - add2] =="X":
        add2 += 1
    return -1 + add1 + add2


for i in range(10):
    for j in range(10):
        if mat[i][j] != ".":
            continue
        mat[i][j] = "X"
        m = max(check_col(i,j), check_row(i,j),check_diagona1(i,j),check_diagona2(i,j))
        if m >= 5:
            print(1)
            exit()
        mat[i][j] = "."
print(0)
        
