# BaekJoon 09/05 2022
# 4179 불!
# 시간초과

import queue
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[False] * C for _ in range(R)]
answer = "IMPOSSIBLE"

fires = []
jihoon = [0, 0]

for i in range(R):
    for j in range(C):
        if board[i][j] == "F":
            fires.append([i, j, 0])
        if board[i][j] == "J":
            jihoon = [i, j, 0]

queue = deque(fires)
while queue:
    x, y, cost = queue.popleft()
    visited[x][y] = True

    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < R and 0 <= dy < C and not visited[dx][dy] and board[dx][dy] == ".":
            board[dx][dy] = cost+1
            queue.append([dx,dy,cost+1])

queue = deque([jihoon])
visited = [[False] * C for _ in range(R)]

while queue:
    x, y, cost = queue.popleft()

    if x == 0 or y == 0 or x == R-1 or y == C-1:
        answer = cost+1
        break

    visited[x][y] = True

    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < R and 0 <= dy < C and not visited[dx][dy]:
            if (type(board[dx][dy]) == int and cost+1 < board[dx][dy]) or (board[dx][dy] == "."):
                queue.append([dx,dy,cost+1])

print(answer)

'''
import queue
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(C)]
dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
visited = [[False] * R for _ in range(C)]
answer = "IMPOSSIBLE"

pos, fires = [0, 0, 0], []

for i in range(C):
    for j in range(R):
        if board[i][j] == "J":
            pos = [i, j, 0]
        if board[i][j] == "F":
            fires.append([i, j])

queue = deque([pos])

flag = False
while True:
    addFires = []
    for f in fires:
        xf, yf = f
        for d in dir:
            xdf, ydf = xf + d[0], yf + d[1]
            if 0 <= xdf < C and 0 <= ydf < R and board[xdf][ydf] == ".":
                board[xdf][ydf] = "F"
                addFires.append([xdf, ydf])
    fires.extend(addFires)
    
    addQueue = []
    while queue:
        x, y, t = queue.popleft()
        visited[x][y] = True

        if (x == 0 or x == C-1 or y ==0 or y == R-1):
            answer = t+1
            flag = True
            break

        for d in dir:
            dx, dy = x + d[0], y + d[1]
            if 0 <= dx < C and 0 <= dy < R and not visited[dx][dy] and board[dx][dy] == ".":
                addQueue.append([dx, dy, t+1])
                board[dx][dy] = "J"
    if not addQueue or flag:
        break
    queue.extend(addQueue)

print(answer)
'''