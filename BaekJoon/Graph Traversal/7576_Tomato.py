from collections import deque


def UDLR(p, n, m):
    point = [[p[0], p[1] - 1], [p[0], p[1] + 1], [p[0] - 1, p[1]], [p[0] + 1, p[1]]]
    move = []

    for pt in point:
        if 0 <= pt[0] < m and 0 <= pt[1] < n and box[pt[0]][pt[1]] == 0:
            move.append(pt)

    return move


N, M = map(int, input().split())
box = []
for _ in range(M):
    box.append(list(map(int, input().split())))

cnt = 0
for i in range(M):
    for j in range(N):
        if box[i][j] == 1 or box[i][j] == -1:
            cnt += 1

queue = deque()
visit = []
days = []

for _ in range(M):
    visit.append([False] * N)
    days.append([0] * N)

for i in range(M):
    for j in range(N):
        if box[i][j] == 1:
            queue.append([i, j])
            days[i][j] = 1

while queue:
    tomato = queue.popleft()
    nextTomato = UDLR(tomato, N, M)

    for n in nextTomato:
        if not visit[n[0]][n[1]]:
            days[n[0]][n[1]] = days[tomato[0]][tomato[1]] + 1
            visit[n[0]][n[1]] = True
            queue.append(n)

flag = False
res = []

for i in range(M):
    for j in range(N):
        if days[i][j] == 0 and box[i][j] != -1:
            flag = True

if cnt == M*N:
    print(0)
elif flag:
    print(-1)
else:
    for i in days:
        res.append(max(i))
    print(max(res)-1)