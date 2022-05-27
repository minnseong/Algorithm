# BaekJoon 05/28 2022
# 1717 집합의 표현

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
n, m = map(int, input().split())
op = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px < py:
        parent[py] = px
    else:
        parent[px] = py

for o in op:
    if o[0] == 0:
        union(o[1], o[2])
    else: # o[0] == 1
        if find(o[1]) == find(o[2]):
            print("YES")
        else:
            print("NO")