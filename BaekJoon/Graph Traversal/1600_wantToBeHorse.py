# BaekJoon 03/03 2023
# 골드3 - 말이 되고픈 원숭이 

import sys
from collections import deque

K = int(input())
W, H = map(int, input().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]

dir = [(0,1), (0,-1), (1,0), (-1,0)]
jump = [(-2,1),(-2,-1),(-1,2),(-1,-2),(1,2),(1,-2),(2,1),(2,-1)]

queue = deque([[0,0,K,0]])
visited = [[[False] * W for _ in range(H)] for _ in range(K+1)]
visited[K][0][0] = True

while queue:
    x, y, k, cost = queue.popleft()

    if x == H-1 and y == W-1:
        print(cost)
        sys.exit()
    
    if k > 0:
        for j in jump:
            dx, dy = x+j[0], y+j[1]
            if 0 <= dx < H and 0 <= dy < W and board[dx][dy] == 0 and not visited[k-1][dx][dy]:
                queue.append([dx,dy,k-1,cost+1])
                visited[k-1][dx][dy] = True

    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < H and 0 <= dy < W and board[dx][dy] == 0 and not visited[k][dx][dy]:
            queue.append([dx,dy,k,cost+1])
            visited[k][dx][dy] = True

print(-1)