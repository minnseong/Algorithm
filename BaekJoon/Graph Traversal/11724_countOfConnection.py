# BaekJoon 03/03 2023
# 실버2 - 연결 요소의 개수

import sys
from collections import defaultdict

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        stack = [i]
        cnt += 1
        while stack:
            s = stack.pop()

            if visited[s]:
                continue
            visited[s] = True
            for g in graph[s]:
                stack.append(g)

print(cnt)