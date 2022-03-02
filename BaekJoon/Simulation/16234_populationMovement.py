# BaekJoon 03/03 2022
# 16234 인구 이동
# Python3 시간초과, PyPy3 통과

import sys
from collections import deque

def calculateDifference(a, b):
    d = abs(board[a[0]][a[1]] - board[b[0]][b[1]])
    if L <= d <= R:
        return 1
    else:
        return 0

def dfs():
    queue = deque([])
    visited = [[False] * N for _ in range(N)]
    dir = [[0,1], [1,0], [-1, 0], [0, -1]]
    global cnt
    cnt = 0

    for x in range(N):
        for y in range(N):
            if visited[x][y] == False:
                queue.append([x, y])
                visited[x][y] = True
                total = 0
                land = []
                while queue:
                    s = queue.popleft()
                    land.append(s)
                    total += board[s[0]][s[1]]
                    for d in dir:
                        dx, dy = s[0]+d[0], s[1]+d[1]
                        if 0 <= dx < N and 0 <= dy < N and not visited[dx][dy] and calculateDifference(s, [dx, dy]):
                            cnt += 1
                            queue.append([dx, dy])
                            visited[dx][dy] = True
                tmp = total // len(land)
                for l in land:
                    board[l[0]][l[1]] = tmp

N, L, R  = map(int, sys.stdin.readline().strip().split())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
cnt = 0

days = 0
while True:
    dfs()
    if cnt == 0:
        break
    days += 1

print(days)