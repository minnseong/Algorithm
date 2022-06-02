# BaekJoon 06/02 2022
# 1647 도시 분할 계획

import sys
input = sys.stdin.readline

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def join(parent, x, y):
    px = find(parent, x)
    py = find(parent, y)

    if px > py:
        parent[px] = py
    else:
        parent[py] = px

n, m = map(int, input().split())
path = [list(map(int, input().split())) for _ in range(m)]
path.sort(key=lambda x: x[2])
res = 0
maxCost = 0
parent = [i for i in range(0, n+1)]

for p in path:
    if find(parent, p[0]) != find(parent, p[1]):
        join(parent, p[0], p[1])
        res += p[2]
        if maxCost < p[2]:
            maxCost = p[2]

print(res-maxCost)