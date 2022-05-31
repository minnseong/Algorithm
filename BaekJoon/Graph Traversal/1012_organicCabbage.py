# BaekJoon 05/31 2022
# 1012 유기농 배추

t = int(input())

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    cnt = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] and not visited[i][j]:
                stack = [[i, j]]
                cnt += 1
                while stack:
                    x, y = stack.pop()
                    visited[x][y] = True
                    for d in dir:
                        dx, dy = x + d[0], y + d[1]
                        if 0 <= dx < n and 0 <= dy < m and board[dx][dy] and not visited[dx][dy]:
                            stack.append([dx, dy])
                        
    print(cnt)