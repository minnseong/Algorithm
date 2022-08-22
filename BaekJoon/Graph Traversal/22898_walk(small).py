# BaekJoon 08/22 2022
# 22868 산책 (small)

import sys
from collections import defaultdict, deque
input = sys.stdin.readline

N, M = map(int, input().split())
path = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    path[a].append(b)
    path[b].append(a)

for key in path.keys():
    path[key].sort()

s, e = map(int, input().split())

queue = deque([[s,[s]]])
visited = [False] * (N+1)
departure_route = set()
arrival_route = set()

res = 0
while queue:
    q, route = queue.popleft()
    visited[q] = True

    if q == e:
        if len(departure_route) == 0 or len(departure_route) > len(route):
            departure_route = set(route)
            
    for p in path[q]:
        if not visited[p]:
            queue.append([p, route+[p]])

departure_route.remove(s)
departure_route.remove(e)

queue = deque([[e,[e]]])
visited = [False] * (N+1)

while queue:
    q, route = queue.popleft()
    visited[q] = True

    if q == s:
        if len(arrival_route) == 0 or len(arrival_route) > len(route):
            arrival_route = set(route)
            
    for p in path[q]:
        if not visited[p] and p not in departure_route:
            queue.append([p, route+[p]])

print(len(departure_route) + len(arrival_route))