# BaekJoon 03/27 2022
# 2636 치즈

import sys
input = sys.stdin.readline

def countOne(board):
    cnt = 0
    for i in range(len(board)):
        cnt += board[i].count(1)
    return cnt

h, w = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
dir = [[1,0], [0,1], [-1,0], [0,-1]]
answer = [0, 0]

while True:
    if not countOne(board):
        break
    else:
        answer[1] = countOne(board)
    stack = [[0,0]]
    visited = [[False] * w for _ in range(h)]
    answer[0] += 1
    while stack:
        y, x = stack.pop()
        visited[y][x] = True
        for d in dir:
            dy, dx = y+d[0], x+d[1]
            if 0 <= dy < h and 0 <= dx < w and not visited[dy][dx]:
                if board[dy][dx] == 1:
                    board[dy][dx] = 0
                elif board[dy][dx] == 0:
                    stack.append([dy, dx])
                visited[dy][dx] = True

for a in answer:
    print(a)

