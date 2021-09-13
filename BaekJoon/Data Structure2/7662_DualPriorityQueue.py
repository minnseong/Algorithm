# BackJoon 09/13 2021
# 7662 DualPriorityQueue

import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    k = int(sys.stdin.readline())
    MaxQueue = []
    MinQueue = []
    cnt = 0

    for _ in range(k):
        cmd = list(sys.stdin.readline().split())
        if cmd[0] == "I":
            num = int(cmd[1])
            heapq.heappush(MaxQueue, num*(-1))
            heapq.heappush(MinQueue, num)
            cnt += 1
        else:
            if cnt == 0:
                MaxQueue = []
                MinQueue = []
            elif cmd[1] == '1':
                heapq.heappop(MaxQueue)
                cnt -= 1
            elif cmd[1] == '-1':
                heapq.heappop(MinQueue)
                cnt -= 1

    if cnt == 0:
        print("EMPTY")
    elif cnt == 1:
        print(str(heapq.heappop(MinQueue)))
    else:
        print(str(heapq.heappop(MaxQueue)*(-1)), end=" ")
        print(str(heapq.heappop(MinQueue)))
