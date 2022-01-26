# BaekJoon 01/25 2022
# 1913 달팽이

N = int(input())
f = int(input()) # 찾고자 하는 숫자

board = [[0]*N for _ in range(N)]
move = [[1,0], [0,1], [-1,0], [0,-1]] # 아래 오른쪽 위 왼쪽
res = []

cur = N ** 2
x, y = 0, 0
dir = 0

while cur > 0:
    board[x][y] = cur
    dx = x + move[dir][0]
    dy = y + move[dir][1]

    if 0 > dx or dx >= N or 0 > dy or dy >= N or board[dx][dy] != 0:
        dir = (dir+1) % 4
    
    x += move[dir][0]
    y += move[dir][1]
    cur -= 1

flag = False
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == f:
            res = [i+1,j+1]
            flag = True
            break
    if flag:
        break

for b in board:
    print(*b)

print(*res)

 
