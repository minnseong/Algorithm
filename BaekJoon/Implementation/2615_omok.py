# BaekJoon 01/31 2022
# 2615 오목

import sys

board = [list(map(int, input().split())) for _ in range(19)]
dir = [[1, 0], [1, 1], [0, 1], [-1, 1]]
winner = list()
flag = False

for x in range(len(board)):
    for y in range(len(board[0])):
        if board[x][y]:
            for d in dir:
                dx = x + d[0]
                dy = y + d[1]

                cnt = 1
                while True:
                    if 0 <= dx < 19 and 0 <= dy < 19:
                        if board[x][y] == board[dx][dy]:
                            cnt += 1
                        else:
                            break
                    else:
                        break
                    dx += d[0]
                    dy += d[1]

                if cnt == 5:
                    if 0 <= x-d[0] < 19 and 0 <= y-d[1] < 19:
                        if board[x][y] != board[x-d[0]][y-d[1]]:
                            winner = [x, y]
                            flag = True
                            break
                    else:
                        winner = [x, y]
                        flag = True
                        break 
        if flag:
            break
    if flag:
        break

if winner:
    x, y = winner[0], winner[1]
    print(board[x][y])
    print(str(x+1) + " " + str(y+1))
else:
    print(0)


                        
