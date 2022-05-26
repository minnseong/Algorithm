# BaekJoon 05/27 2022
# 1922 네트워크 연결

import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    px = find(parent, x)
    py = find(parent, y)

    if px > py:
        parent[px] = py
    else:
        parent[py] = px

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(m)]

graph.sort(key=lambda x : x[2])
parent = [i for i in range(n+1)]
res = 0

for g in graph:
    a, b, c = g
    if find(parent, a) != find(parent, b):
        res += c
        union(parent, a, b)

print(res)