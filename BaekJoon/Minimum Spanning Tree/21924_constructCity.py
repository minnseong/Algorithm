# BaekJoon 06/12 2022
# 21924 도시 건설

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
    
N, M = map(int, input().split())
parent = [i for i in range(N+1)]
answer = 0
cnt = 0

path = []
for i in range(M):
    a, b, cost = map(int, input().split())
    answer += cost
    path.append([a, b, cost])

path.sort(key=lambda x : x[2])

for p in path:
    if find(parent, p[0]) != find(parent, p[1]):
        union(parent, p[0], p[1])
        answer -= p[2]
        cnt += 1

if cnt != N-1:
    print(-1)
else:
    print(answer)