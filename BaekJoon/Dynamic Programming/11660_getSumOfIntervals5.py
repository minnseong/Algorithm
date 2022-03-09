# BaekJoon 03/09 2022
# 11660 구간 합 구하기 5

import sys

n, m = map(int, sys.stdin.readline().strip().split())
board = [[0] for _ in range(n+1)]

for i in range(0, n+1):
    if i == 0:
        board[i].extend([0] * n)
    else:
        board[i].extend(list(map(int, sys.stdin.readline().strip().split())))

for i in range(len(board)):
    for j in range(len(board[0])):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            board[i][j] += board[i][j-1]
        elif j == 0:
            board[i][j] += board[i-1][j]
        else:
            board[i][j] += (board[i][j-1] + board[i-1][j] - board[i-1][j-1])

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    print(board[x2][y2] - board[x2][y1-1] - board[x1-1][y2] + board[x1-1][y1-1])