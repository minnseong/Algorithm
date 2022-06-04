# BaekJoon 06/04 2022
# 16398 행성 연결

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
    
N = int(input())
answer = 0
flow = []

rg = 1
for i in range(N):
    j = 0
    for cost in (list(map(int, input().split()))):
        if j < rg:
            flow.append([i, j, cost])
            j += 1
        else:
            break
    rg += 1

flow.sort(key=lambda x : x[2])
parent = [i for i in range(N)]

for f in flow:
    if find(parent, f[0]) != find(parent, f[1]):
        union(parent, f[0], f[1])
        answer += f[2]

print(answer)