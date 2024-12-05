t = int(input())
apt=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]]
for i in range(1,15):  
    apt.append([0])
    for j in range(1,15):   
        apt[i].append(apt[i][j-1] +apt[i-1][j])
for i in range(t):
    k = int(input())
    n = int(input())
    print(apt[k][n])
    