# BaekJoon 03/02 2023
# 골드2 - 물대기

import sys, heapq

N = int(input())

heap = []
for i in range(1, N+1):
    heapq.heappush(heap, [int(sys.stdin.readline()), i, 0])

for i in range(N):
    v = list(map(int, sys.stdin.readline().split()))
    for j in range(i+1, N):
        heapq.heappush(heap, [v[j], i+1, j+1])

global parents
parents = [i for i in range(N+1)]

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        if px > py:
            parents[px] = py
        else:
            parents[py] = px

answer = 0
while heap:
    cost, x, y = heapq.heappop(heap)

    if find(x) != find(y):
        answer += cost
        union(x, y)
print(answer)