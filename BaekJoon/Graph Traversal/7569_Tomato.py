from collections import deque
import sys


def UDLRFB(p, m, n, h):
    # point (층, 위아래, 왼오른)
    direction = {'UP': [p[0]+1, p[1], p[2]], 'DOWN': [p[0]-1, p[1], p[2]], 'LEFT': [p[0], p[1], p[2]-1],
                 'RIGHT': [p[0], p[1], p[2]+1], 'FRONT': [p[0], p[1]+1, p[2]], 'BACK': [p[0], p[1]-1, p[2]]}

    move = []
    for d in direction.values():
        if 0 <= d[0] < h and 0 <= d[1] < n and 0 <= d[2] < m:
            move.append(d)

    return move


M, N, H = map(int, sys.stdin.readline().split())
box = []

for j in range(H):
    stair = []
    for i in range(N):
        stair.append(list(map(int, sys.stdin.readline().split())))
    box.append(stair)

queue = deque()
visit = []
days = []

for h in range(H):
    tmp = []
    temp = []
    for i in range(N):
        tmp.append([False] * M)
        temp.append([0] * M)
        for j in range(M):
            if box[h][i][j] == 1:
                queue.append([h, i, j])
                temp[i][j] = 1
    visit.append(tmp)
    days.append(temp)

while queue:
    node = queue.popleft()
    nextTomato = UDLRFB(node, M, N, H)

    for n in nextTomato:
        if not visit[n[0]][n[1]][n[2]] and box[n[0]][n[1]][n[2]] == 0:
            visit[n[0]][n[1]][n[2]] = True
            days[n[0]][n[1]][n[2]] = days[node[0]][node[1]][node[2]] + 1
            queue.append(n)

flag = False
cnt = 0
maxDay = []

for h in range(H):
    for i in range(N):
        tmp = []
        for j in range(M):
            if days[h][i][j] == 0 and box[h][i][j] != -1:
                flag = True
            if box[h][i][j] == -1 or box[h][i][j] == 1:
                cnt += 1
            tmp.append(days[h][i][j])
        maxDay.append(max(tmp))

if flag:
    print(-1)
elif cnt == H*M*N:
    print(0)
else:
    print(max(maxDay)-1)