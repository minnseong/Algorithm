# BackJoon 03/02 2023
# 골드2 - 보석도둑

import sys
import heapq

N, K = map(int, input().split())

jewels = list()
for _ in range(N):
    jewels.append(list(map(int, sys.stdin.readline().split())))

bags = list()
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

bags.sort()
jewels.sort(key=lambda x: -x[0])
q = list()

answer = 0
for b in bags:
    while jewels and jewels[-1][0] <= b:
        m, k = jewels.pop()
        heapq.heappush(q, [-k, m])
    if q:
        k, m = heapq.heappop(q)
        answer += abs(k)

print(answer)
