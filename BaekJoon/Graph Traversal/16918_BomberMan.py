from collections import deque


def findBomb():
    res = []

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'O':
                res.append([r, c])

    return res


R, C, N = map(int, input().split())
grid = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for i in range(R):
    grid.append(list(input()))

if N == 1:
    for i in grid:
        print(''.join(i))

elif N % 2 == 0:
    for i in range(R):
        print('O'*C)

else:
    for c in range(int(N/2)):
        queue = deque()
        queue.extend(findBomb())
        visit = []

        for i in range(R):
            visit.append([False] * C)

        while queue:
            bomb = queue.popleft()
            visit[bomb[0]][bomb[1]] = True

            for i in range(4):
                if 0 <= bomb[0]-dx[i] < R and 0 <= bomb[1]-dy[i] < C:
                    visit[bomb[0]-dx[i]][bomb[1]-dy[i]] = True

        for i in range(R):
            for j in range(C):
                if visit[i][j]:
                    grid[i][j] = '.'
                else:
                    grid[i][j] = 'O'

    for i in grid:
        print(''.join(i))
