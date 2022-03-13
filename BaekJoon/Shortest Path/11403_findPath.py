# BaekJoon 03/13 2022
# 11403 경로 찾기

'''
플로이드-워셜 알고리즘으로 풀이

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1
'''
import copy

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
loc = [list() for _ in range(n)]

for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j]:
            loc[i].append(j)

for i in range(len(graph)):
    visited = [False] * n
    stack = copy.deepcopy(loc[i])
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = True
        graph[i][node] = 1

        stack.extend(loc[node])

for g in graph:
    print(*g)