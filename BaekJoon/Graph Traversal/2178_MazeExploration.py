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

for i in range(N):
    tmp = ''.join(input().split())
    maze.append(tmp)

queue = deque([[0, 0]])
visit = []
cnt = 0
for _ in range(N):
    visit.append([False] * M)

moveCnt = 0

while queue:
    node = queue.popleft()
    if node == [N-1, M-1]:
        visit[node[0]][node[1]] = True
        print(moveCnt - 1)
        break

    nextMove = UDLR(node, N, M, maze)

    if not visit[node[0]][node[1]]:
        visit[node[0]][node[1]] = True
        moveCnt += 1
        queue.extend(nextMove)