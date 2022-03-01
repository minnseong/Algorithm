# BaekJoon 03/01 2022
# 14502 연구실

import sys
from collections import deque
from itertools import combinations
import copy

def bfs(copy_board):
    queue = deque()
    cnt = 0

    for i in range(N):
        for j in range(M):
            if copy_board[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        for d in dir:
            dx, dy = x + d[0], y + d[1]
            if 0 <= dx < N and 0 <= dy < M and copy_board[dx][dy] == 0:
                copy_board[dx][dy] = 2
                queue.append((dx, dy))
    
    for b in copy_board:
        cnt += b.count(0)
    return cnt

def makeWall():
    loc = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                loc.append([i, j])
    
    combi = list(combinations(loc, 3))
    return combi

N, M = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
ans = 0

combi = makeWall()
for cb in combi:
    copy_board = copy.deepcopy(board)
    for c in cb:
        copy_board[c[0]][c[1]] = 1
    if ans < bfs(copy_board):
        ans = bfs(copy_board)

print(ans)