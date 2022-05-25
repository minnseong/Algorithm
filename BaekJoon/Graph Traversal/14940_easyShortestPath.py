# BaekJoon 05/25 2022
# 14940 쉬운 최단거리

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
res = [[0] * m for _ in range(n)]
dest = []

flag = False
for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == 2:
            dest = [i, j]
            flag = True
            break
    if flag:
        break

dir = [[1,0], [-1,0], [0,1], [0,-1]]
visited = [[False] * m for _ in range(n)]
queue = deque([(dest[0], dest[1], 0)])
visited[dest[0]][dest[1]] = True

while queue:
    x, y, d = queue.popleft()
    res[x][y] = d

    for dr in dir:
        dx, dy = x + dr[0], y + dr[1]
        if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy]:
            if maps[dx][dy] != 0:
                queue.append((dx, dy, d+1))
                visited[dx][dy] = True

for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] == 1 and res[i][j] == 0:
            res[i][j] = -1

for r in res:
    print(*r)