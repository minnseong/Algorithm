# BaekJoon 05/27 2022
# 13975 파일 합치기 3

import heapq

t = int(input())

for _ in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    res = 0

    while len(files) != 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        res += (a + b)
        heapq.heappush(files, a+b)
    
    print(res)
