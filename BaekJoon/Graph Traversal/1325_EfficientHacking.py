import sys
from collections import deque

input = sys.stdin.readline

N, M = input().split()
edge = []
for _ in range(int(M)):
    edge.append(list(map(int, input().split())))

graph = {}
for g in edge:
    if g[1] not in graph:
        graph[g[1]] = [g[0]]
    else:
        graph[g[1]].append(g[0])


def bfs(graph_, start, n):
    queue = deque([start])
    visit = [False] * n
    cnt = 0

    while queue:
        node = queue.popleft()
        cnt += 1
        if not visit[node - 1]:
            visit[node - 1] = True
            if node in graph_:
                queue.extend(graph_[node])

    return cnt


cntList = []
for i in range(int(M)):
    cntList.append(bfs(graph, i + 1, int(N)))

maxCnt = max(cntList)
for i in range(int(M)):
    if cntList[i] == maxCnt:
        print(i+1, end=" ")