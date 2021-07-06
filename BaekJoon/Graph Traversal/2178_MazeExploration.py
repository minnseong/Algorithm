from collections import deque


def UDLR(p, n, m, maze):
    point = [[p[0], p[1]-1], [p[0], p[1]+1], [p[0]-1, p[1]], [p[0]+1, p[1]]]
    move = []

    for pt in point:
        if 0 <= pt[0] < n and 0 <= pt[1] < m and maze[pt[0]][pt[1]] == '1':
            move.append(pt)

    return move


N, M = map(int, input().split())
maze = []
path = [[0]*M for _ in range(N)]

for i in range(N):
    tmp = ''.join(input().split())
    maze.append(tmp)

queue = deque([[0, 0]])
visit = []
for _ in range(N):
    visit.append([False] * M)

while queue:
    node = queue.popleft()
    nextMove = UDLR(node, N, M, maze)

    for m in nextMove:
        if not visit[m[0]][m[1]]:
            queue.append(m)
            path[m[0]][m[1]] = path[node[0]][node[1]] + 1
            visit[m[0]][m[1]] = True

print(path[N-1][M-1] + 1)