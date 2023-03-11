# BaekJoon 03/11 2023
# 1197 최소 스패닝 트리

import sys

V, E = map(int, input().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
graph.sort(key=lambda x:x[2])

global parents
parents = [i for i in range(V+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x_parent = find(x)
    y_parent = find(y)

    if x_parent != y_parent:
        if x_parent > y_parent:
            parents[x_parent] = y_parent
        else:
            parents[y_parent] = x_parent

answer = 0
for g in graph:
    x, y, cost = g
    if find(x) != find(y):
        answer += cost
        union(x, y)

print(answer)