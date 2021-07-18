import sys
import heapq as hq

N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-hq.heappop(heap))
    else:
        hq.heappush(heap, -x)