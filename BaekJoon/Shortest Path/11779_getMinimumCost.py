# BaekJoon 03/07 2023
# 골드3 - 최소비용 구하기 2

import sys
import heapq
from collections import defaultdict

n = int(input())
m = int(input())

graph = defaultdict(list)

for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

start, end = map(int, input().split())

distance = [1e9] * (n+1)
heap = []
heapq.heappush(heap, [0, start])
distance[start] = 0
prev = [0] * (n+1)

while heap:
    dt, node = heapq.heappop(heap)

    if distance[node] != dt:
        continue
    
    for n in graph[node]:
        cost = dt + n[1]

        if distance[n[0]] > cost:
            distance[n[0]] = cost
            prev[n[0]] = node
            heapq.heappush(heap, [cost, n[0]])

print(distance[end])

dist = [end]
prv = end
while prv != start:
    prv = prev[prv]
    dist.append(prv)

print(len(dist))
for d in reversed(dist):
    print(d, end=" ")