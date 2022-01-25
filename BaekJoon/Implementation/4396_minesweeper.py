# BaekJoon 01/25 2022
# 4396 지뢰찾기

import sys

def checkMine(loc):
    global board
    mine = 0
    x, y = loc[0], loc[1]
    direction = [[1,0],[-1,0],[0,1],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
    
    for d in direction:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < len(board[0]) and 0 <= dy < len(board):
            if board[dx][dy] == "*":
                mine += 1
    
    return str(mine)


n = int(input())
answer = []
flag = False

board = [list(sys.stdin.readline().strip()) for i in range(n)]
openBoard = [list(sys.stdin.readline().strip()) for i in range(n)]

for i in range(len(openBoard)):
    tmp = []
    for j in range(len(openBoard[0])):
        if openBoard[i][j] == 'x' and board[i][j] == '*':
            flag = True

        if openBoard[i][j] == 'x' and board[i][j] != '*':
            tmp.append(checkMine([i,j]))
        else:
            tmp.append(".")
    
    answer.append(tmp)

if flag:
    for i in range(len(answer)):
        for j in range(len(answer[0])):
            if board[i][j] == "*":
                answer[i][j] = "*"
                
for a in answer:
    print(''.join(a))