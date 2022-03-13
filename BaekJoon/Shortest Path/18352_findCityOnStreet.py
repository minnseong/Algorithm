# BaekJoon 03/13 2022
# 18352 특정 거리의 도시 찾기

from collections import deque
import math
import sys

n, m, k, x = map(int, input().split())
loc = dict()
distance = [math.inf] * (n+1)
distance[x] = 0
visited = [False] * (n+1)
visited[x] = True
cnt = 0

for _ in range(m):
    s, e = map(int, sys.stdin.readline().strip().split())
    if s in loc:
        loc[s].append(e)
    else:
        loc[s] = [e]

queue = deque([])
for l in loc[x]:
    queue.append([l, 1])

while queue:
    node, path = queue.popleft()
    if distance[node] > path:
        distance[node] = path
    
    if not visited[node] and node in loc:
        for l in loc[node]:
            queue.append([l, path+1])
        visited[node] = True

for idx, val in enumerate(distance):
    if val == k:
        print(idx)
        cnt += 1

if not cnt:
    print(-1)