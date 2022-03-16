# BaekJoon 03/16 2022
# 5547 일루미네이션
    
from collections import deque

w, h = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(h)]
visited = [[False] * w for _ in range(h)]
answer = 0
odd_dir = [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]]
even_dir = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]]

#  00 01 02 03 04 05 06 07
# 10 11 12 13 14 15 16 17
#  20 21 22 23 24 25 26 27
# 30 31 32 33 34 35 36 37

def buildingDfs(xx, yy):
    stack = [[xx, yy]]
    visited[xx][yy] = True
    cnt = 0

    while stack:
        x, y = stack.pop()
        cnt += 6
        if x & 1:
            dir = odd_dir
        else:
            dir = even_dir

        for d in dir:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < h and 0 <= dy < w and maps[dx][dy]:
                cnt -= 1
            if 0 <= dx < h and 0 <= dy < w and maps[dx][dy] and not visited[dx][dy]: 
                stack.append([dx, dy])
                visited[dx][dy] = True
    
    return cnt

def noBuildingDfs(xx, yy):
    stack = [[xx, yy]]
    visited[xx][yy] = True
    flag = True
    cnt = 0

    while stack:
        x, y = stack.pop()
        if x == 0 or x == h-1 or y == 0 or y == w-1:
            flag = False
        cnt += 6
        if x & 1:
            dir = odd_dir
        else:
            dir = even_dir

        for d in dir:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < h and 0 <= dy < w and not maps[dx][dy]:
                cnt -= 1
            if 0 <= dx < h and 0 <= dy < w and not maps[dx][dy] and not visited[dx][dy]: 
                stack.append([dx, dy])
                visited[dx][dy] = True
    if flag:
        return cnt
    else:
        return 0

for i in range(len(maps)):
    for j in range(len(maps[0])):
        if maps[i][j] and not visited[i][j]:
            answer += buildingDfs(i, j)
        elif not maps[i][j] and not visited[i][j]:
            answer -= noBuildingDfs(i, j)

print(answer)