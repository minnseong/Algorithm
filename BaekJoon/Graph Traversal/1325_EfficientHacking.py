from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
edge = []
for _ in range(M):
    edge.append(list(map(int, sys.stdin.readline().split())))

graph = {}
for g in edge:
    if g[1] not in graph:
        graph[g[1]] = [g[0]]
    else:
        graph[g[1]].append(g[0])

check = [False for _ in range(N)]
for i in graph:
    check[i-1] = True


def bfs(graph_, start, n):
    queue = deque([start])
    visit = [False for _ in range(n)]

    cnt = 0

    while queue:
        node = queue.popleft()
        cnt += 1
        if not visit[node - 1]:
            visit[node - 1] = True
            if check[node-1]:
                queue.extend(graph_[node])

    return cnt


cntList = []
for i in range(N):
    if check[i]:
        cntList.append(bfs(graph, i + 1, N))
    else:
        cntList.append(0)

maxCnt = max(cntList)

for i in range(M):
    if cntList[i] == maxCnt:
        print(i+1, end=" ")