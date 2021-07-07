def UDLR(p, n):
    point = [[p[0], p[1] - 1], [p[0], p[1] + 1], [p[0] - 1, p[1]], [p[0] + 1, p[1]]]
    move = []

    for pt in point:
        if 0 <= pt[0] < n and 0 <= pt[1] < n and estate[pt[0]][pt[1]] == '1':
            move.append(pt)

    return move


N = int(input())
estate = []
visit = []
cnt = []

for _ in range(N):
    estate.append(input())
    visit.append([False] * N)

for i in range(N):
    for j in range(N):
        if estate[i][j] == '1' and not visit[i][j]:
            stack = [[i, j]]
            count = 0
            while stack:
                house = stack.pop()
                nextHouse = UDLR(house, N)

                if not visit[house[0]][house[1]]:
                    visit[house[0]][house[1]] = True
                    count += 1
                    stack.extend(nextHouse)

            cnt.append(count)

print(len(cnt))
cnt.sort()
for c in cnt:
    print(c)
