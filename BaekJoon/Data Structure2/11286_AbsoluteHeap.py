import sys
import heapq as hq

N = int(sys.stdin.readline().strip())
heap = []
ans = []
hh = 0

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(heap) == 0:
            ans.append(0)
        else:
            h = hq.heappop(heap)[1]
            ans.append(h)

    else:
        hq.heappush(heap, [abs(x), x])

for a in ans:
    print(a)