import sys

n, m = map(int, sys.stdin.readline().split())
mat = []

for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().split())))

class Shapes:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y
        self.possible_shape = []    

    def biggest(self):
        sums = []
        for Coordinates in self.possible_shape:
            sum = 0
            for Coordinate in Coordinates:
                sum += mat[Coordinate[0]][Coordinate[1]]
            sums.append(sum)
        if sums:
            sums.sort()
            return sums[-1]
        return 0    
        
class shape1(Shapes): # 일자형
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        if self.start_x + 3 < len(mat):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x + 1, self.start_y), (self.start_x + 2, self.start_y), (self.start_x + 3, self.start_y)])
        if self.start_y + 3 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x, self.start_y + 1), (self.start_x, self.start_y + 2), (self.start_x, self.start_y + 3)])

class shape2(Shapes): #정사각형
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        if self.start_x + 1 < len(mat) and self.start_y + 1 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x + 1, self.start_y), (self.start_x + 1, self.start_y + 1), (self.start_x, self.start_y + 1)])

class shape3(Shapes): #ㄱ자형
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        if self.start_x - 2 >= 0 and self.start_y + 1 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x - 1, self.start_y), (self.start_x - 2, self.start_y), (self.start_x, self.start_y + 1)])

        if self.start_x - 2 >= 0 and self.start_y - 1 >= 0:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x - 1, self.start_y), (self.start_x - 2, self.start_y), (self.start_x, self.start_y - 1)])

        if self.start_x + 2 < len(mat) and self.start_y - 1 >= 0:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x + 1, self.start_y), (self.start_x + 2, self.start_y), (self.start_x, self.start_y - 1)])

        if self.start_x + 2 < len(mat) and self.start_y + 1 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x + 1, self.start_y), (self.start_x + 2, self.start_y), (self.start_x, self.start_y + 1)])

        if self.start_x - 1 >= 0 and self.start_y - 2 >= 0:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x - 1, self.start_y), (self.start_x, self.start_y - 1), (self.start_x, self.start_y - 2)])

        if self.start_x + 1 < len(mat) and self.start_y - 2 >= 0:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x + 1, self.start_y), (self.start_x, self.start_y - 1), (self.start_x, self.start_y - 2)])

        if self.start_x - 1 >= 0 and self.start_y + 2 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x - 1, self.start_y), (self.start_x, self.start_y + 1), (self.start_x, self.start_y + 2)])
   
        if self.start_x + 1 < len(mat) and self.start_y + 2 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x + 1, self.start_y), (self.start_x, self.start_y + 1), (self.start_x, self.start_y + 2)])

class shape4(Shapes): #ㄹ자형
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        if self.start_x - 1 >= 0 and 1 <= self.start_y < len(mat[0]) - 1:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x - 1, self.start_y), (self.start_x - 1, self.start_y + 1), (self.start_x, self.start_y - 1)])
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x - 1, self.start_y), (self.start_x - 1, self.start_y - 1), (self.start_x, self.start_y + 1)])

        if 1 <= self.start_x < len(mat) - 1 and self.start_y + 1 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x, self.start_y + 1), (self.start_x - 1, self.start_y + 1), (self.start_x + 1, self.start_y)])
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x, self.start_y + 1), (self.start_x + 1, self.start_y + 1), (self.start_x - 1, self.start_y)])

class shape5(Shapes): #ㅗ자형
    def __init__(self, start_x, start_y):
        super().__init__(start_x, start_y)
        if self.start_x - 1 >= 0 and 1 <= self.start_y < len(mat[0]) - 1:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x - 1, self.start_y), (self.start_x, self.start_y - 1), (self.start_x, self.start_y + 1)])

        if self.start_x + 1 < len(mat) and 1 <= self.start_y < len(mat[0]) - 1:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x + 1, self.start_y), (self.start_x, self.start_y - 1), (self.start_x, self.start_y + 1)])

        if 1 <= self.start_x < len(mat) - 1 and self.start_y + 1 < len(mat[0]):
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x, self.start_y + 1), (self.start_x - 1, self.start_y), (self.start_x + 1, self.start_y)])

        if 1 <= self.start_x < len(mat) - 1 and self.start_y - 1 >= 0:
            self.possible_shape.append([(self.start_x, self.start_y), (self.start_x, self.start_y - 1), (self.start_x - 1, self.start_y), (self.start_x + 1, self.start_y)])

biggest_sum = 0
sums = []

for i in range(n):
    for j in range(m):
        a = shape1(i ,j)
        b = shape2(i ,j)
        c = shape3(i ,j)
        d = shape4(i ,j)
        e = shape5(i ,j)
        sums.append(a.biggest())
        sums.append(b.biggest())
        sums.append(c.biggest())
        sums.append(d.biggest())
        sums.append(e.biggest())

sums.sort()
print(sums[-1])
