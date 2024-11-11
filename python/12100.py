from collections import deque
import copy

n = int(input())

board = [[0 for _ in range(n)] for _ in range(n)]

biggest = 0
board_q = deque()

for i in range(n):
    board[i] = list(map(int, input().split(" ")))
    if max(board[i]) > biggest:
        biggest = max(board[i])

board_q.append((board, 0))  # 큐에 보드 상태와 깊이를 함께 저장

def push_line(line):
    global biggest
    l = len(line)
    new_line = [0 for _ in range(l)]
    not_added = [True for _ in range(l)]
    first = True
    count = 0
    for i in range(l):
        if line[i] != 0:
            if first:
                new_line[count] = line[i]
                first = False

            elif line[i] != new_line[count] or not not_added[count]:
                count += 1
                new_line[count] = line[i]

            elif line[i] == new_line[count] and not_added[count]:
                if i == count:
                    continue
                new_line[count] += line[i]
                if new_line[count] > biggest:
                    biggest = new_line[count]
                not_added[count] = False
    return new_line

def push_matrix(matrix, dir, m):
    new_mat = [[0 for _ in range(m)] for _ in range(m)]
    if dir == 1:
        for i in range(m):
            new_mat[i] = push_line(matrix[i])
    if dir == 2:
        for i in range(m):
            line = list(reversed(matrix[i]))
            new_mat[i] = list(reversed(push_line(line)))
    if dir == 3:
        transposed = list(zip(*matrix))
        transposed_pushed = [push_line(list(row)) for row in transposed]
        new_mat = [list(row) for row in zip(*transposed_pushed)]
    if dir == 4:
        transposed = list(zip(*matrix))
        transposed_pushed = [list(reversed(push_line(list(reversed(row))))) for row in transposed]
        new_mat = [list(row) for row in zip(*transposed_pushed)]
    return new_mat

dir_list = [1, 2, 3, 4]
visited = set()

while board_q:
    now_mat, depth = board_q.popleft()
    if depth == 5:
        continue
    for dir in dir_list:
        new_mat = push_matrix(now_mat, dir, n)
        new_mat_tuple = tuple(tuple(row) for row in new_mat)
        if new_mat_tuple not in visited:
            visited.add(new_mat_tuple)
            board_q.append((new_mat, depth + 1))

print(biggest)
