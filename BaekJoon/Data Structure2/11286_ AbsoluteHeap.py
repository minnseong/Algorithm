import sys
import heapq as hq

N = int(sys.stdin.readline().strip())
heap = []
tmp = []
flag = True

for _ in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            h = hq.heappop(heap)
            if len(tmp) != 0 and flag:
                hh = hq.heappop(tmp)

            if h == hh:
                print(-h)
                flag = True
            else:
                print(h)
                flag = False
    elif x > 0:
        hq.heappush(heap, x)
    else:
        hq.heappush(heap, -x)
        hq.heappush(tmp, -x)



