# Programmers 02/27 2023
# 골드2 - 퍼즐

import sys
from collections import deque

puzzle = ""
for _ in range(3):
    a, b, c = map(str, sys.stdin.readline().split())
    puzzle += (a + b + c)

dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

queue = deque([puzzle])
visited = dict()
visited[puzzle] = 0

while queue:
    p = queue.popleft()

    if p == "123456780":
        print(visited[p])
        sys.exit()
    
    index = p.index('0')
    x = index // 3
    y = index % 3

    for d in dir:
        dx, dy = x+d[0], y+d[1]
        if 0 <= dx < 3 and 0 <= dy < 3:
            tmp = list(p)
            tmp[x*3+y] = tmp[dx*3+dy]
            tmp[dx*3+dy] = '0'
            tmp = ''.join(tmp)
            if tmp not in visited:
                queue.append(tmp)
                visited[tmp] = (visited[p] + 1)

print(-1)