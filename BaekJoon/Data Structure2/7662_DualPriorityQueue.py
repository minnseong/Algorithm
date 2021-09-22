# BaekJoon 09/22 2021
# 7662 이중 우선순위 큐

import sys
import heapq

T = int(sys.stdin.readline())
syncDic = {}

for _ in range(T):
    k = int(sys.stdin.readline())
    cnt = 0

    for _ in range(k):
        cmd = list(sys.stdin.readline().split())

        if cnt == 0:
            MaxQueue = []
            MinQueue = []

        if cmd[0] == "I":
            num = int(cmd[1])
            heapq.heappush(MaxQueue, num*(-1))
            heapq.heappush(MinQueue, num)
            if num in syncDic:
                syncDic[num] += 1
            else:
                syncDic[num] = 1
            cnt += 1
            print(syncDic)
        else:
            if cnt == 0:
                pass
            elif cmd[1] == '1':
                while True:
                    h = heapq.heappop(MaxQueue) * (-1)
                    if syncDic[h] == 0:
                        pass
                    else:
                        syncDic[h] -= 1
                        break
                cnt -= 1

            elif cmd[1] == '-1':
                while True:
                    h = heapq.heappop(MinQueue)
                    if syncDic[h] == 0:
                        pass
                    else:
                        syncDic[h] -= 1
                        break
                cnt -= 1

    if cnt == 0:
        print("EMPTY")
    else:
        print(str(heapq.heappop(MaxQueue)*(-1)), end=" ")
        print(str(heapq.heappop(MinQueue)))
