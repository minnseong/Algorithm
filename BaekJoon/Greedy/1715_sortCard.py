# BaekJoon 05/30 2022
# 1715 카드 정렬하기

import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = [int(input()) for _ in range(n)]
heapq.heapify(heap)
res = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    res += (a + b)
    heapq.heappush(heap, a+b)

print(res)