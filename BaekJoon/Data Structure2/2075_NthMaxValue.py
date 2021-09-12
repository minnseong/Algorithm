# BaekJoon 09/12 2021
# 2075 N번째 큰 수
import heapq
import sys

N = int(input())
heap = []

for i in range(N):
    arr = list(map(int, input().split()))
    if not heap:
        for j in arr:
            heapq.heappush(heap, j)
    else:
        for j in arr:
            if heap[0] < j:
                heapq.heappop(heap)
                heapq.heappush(heap, j)

print(heap[0])
