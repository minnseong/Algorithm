# BaekJoon 08/16 2022
# 18513 샘터

import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
spring = list(map(int, input().split()))
queue = deque()
visited = defaultdict(bool)
res = 0

for s in spring:
    visited[s] = True
    queue.append([s, 0])

while queue:
    q, v = queue.popleft()

    if not visited[q+1]:
        res += (v+1)
        visited[q+1] = True
        queue.append([q+1, v+1])
        K -= 1

    if K == 0:
        break

    if not visited[q-1]:
        res += (v+1)
        visited[q-1] = True
        queue.append([q-1, v+1])
        K -= 1

    if K == 0:
        break

print(res)