# BaekJoon 06/01 2022
# 1976 여행 가자

import sys

input = sys.stdin.readline
n = int(input())
m = int(input())

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

for i in range(1, n+1):
    graph = list(map(int, input().split()))
    for j in range(len(graph)):
        if graph[j] == 1:
            union(i, j+1)

plan = list(map(int, input().split()))
p = find(plan[0])

flag = False
for i in range(1, len(plan)):
    if find(plan[i]) != p:
        flag = True
        break

if flag:
    print("NO")
else:
    print("YES")
    
