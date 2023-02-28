# Programmers 02/28 2023
# 골드2 - 2048 (Easy)

def up(board, n):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[j][i] != 0:
                tmp = board[j][i]
                board[j][i] = 0
                if board[pointer][i] == 0:
                    board[pointer][i] = tmp
                elif board[pointer][i] == tmp:
                    board[pointer][i] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[pointer][i] = tmp
    return board

def down(board, n):
    for i in range(n):
        pointer = n - 1
        for j in range(n-2, -1, -1):
            if board[j][i] != 0:
                tmp = board[j][i]
                board[j][i] = 0
                if board[pointer][i] == 0:
                    board[pointer][i] = tmp
                elif board[pointer][i] == tmp:
                    board[pointer][i] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[pointer][i]= tmp
    return board

def left(board, n):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer] = tmp

    return board

def right(board, n):
    for i in range(n):
        pointer = n-1
        for j in range(n-2, -1 , -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer] == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board

import sys, copy

N = int(sys.stdin.readline())

board = list()
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

stack = [[board, 0]]
answer = 0

while stack:
    board, cnt = stack.pop()

    if cnt == 5:
        for b in board:
            answer = max(answer, max(b))
        continue

    stack.append([up(copy.deepcopy(board), N), cnt+1])
    stack.append([down(copy.deepcopy(board), N), cnt+1])
    stack.append([left(copy.deepcopy(board), N), cnt+1])
    stack.append([right(copy.deepcopy(board), N), cnt+1])

print(answer)
