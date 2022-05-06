# BaekJoon 05/07 2022
# 1753 최단 경로

import sys
import math
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = math.inf

n, m = map(int, input().split())
start = int(input())

graph = defaultdict(list)
visited = [False] * (n+1)
distance = [INF] * (n+1)
heap = []

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])

def get_smallest_node():
    while heap:
        d, n = heapq.heappop(heap)
        if not visited[n]:
            return n
    return -1

def dijkstra(node):
    visited[node] = True
    distance[start] = 0

    for g in graph[node]:
        if distance[g[0]] > g[1]: # 서로 다른 두 node에 여러개의 간선이 있을 수 있다.
            distance[g[0]] = g[1]
        heapq.heappush(heap, (g[1], g[0]))
    
    for _ in range(n-1):
        nextNode = get_smallest_node()
        if nextNode == -1:
            break
        visited[nextNode] = True

        for nn in graph[nextNode]:
            if distance[nn[0]] > distance[nextNode] + nn[1]:
                distance[nn[0]] = distance[nextNode] + nn[1]
                heapq.heappush(heap, (distance[nn[0]], nn[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])