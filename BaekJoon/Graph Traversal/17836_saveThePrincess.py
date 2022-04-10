# BaekJoon 04/10 2022
# 17836 공주님을 구해라!

from collections import deque

n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
res = []

queue = deque()
visited = [[False] * m for _ in range(n)]
dir = [[1,0], [0,1], [0,-1], [-1,0]]

queue.append([0,0,0])
visited[0][0] = True

while queue:
    x, y, c = queue.popleft()

    if board[x][y] == 2:
        res.append(c + (n-1-x) + (m-1-y))
    if x == n-1 and y == m-1:
        res.append(c)
        break

    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and board[dx][dy] != 1:
            queue.append([dx, dy, c+1])
            visited[dx][dy] = True

if res and min(res) <= t:
    print(min(res))
else:
    print("Fail")