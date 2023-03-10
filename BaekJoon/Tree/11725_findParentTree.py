# BaekJoon 03/10 2023
# 실버2 - 트리의 부모 찾기

from collections import defaultdict, deque

N = int(input())

graph = defaultdict(list)

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

parents = [0] * (N+1)
queue = deque([1])
visited = [False] * (N+1)

while queue:
    q = queue.popleft()

    if visited[q]:
        continue
    visited[q] = True

    for g in graph[q]:
        if parents[g] == 0:
            parents[g] = q
        queue.append(g)

for p in parents[2:]:
    print(p)