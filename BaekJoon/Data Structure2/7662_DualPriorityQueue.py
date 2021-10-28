# BaekJoon 09/22 2021
# 7662 이중 우선순위 큐
# commit error

import sys
import heapq

def sync(num):
    if syncDic[num] == 0:
        return False
    else:
        syncDic[num] -= 1
        return True

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
        else:
            if cnt == 0:
                pass
            elif cmd[1] == '1':
                while True:
                    h = heapq.heappop(MaxQueue) * (-1)
                    if sync(h):
                        break
                cnt -= 1

            elif cmd[1] == '-1':
                while True:
                    h = heapq.heappop(MinQueue)
                    if sync(h):
                        break
                cnt -= 1
    
    if cnt == 0:
        print("EMPTY")
    else:
        while True:
            h = heapq.heappop(MaxQueue) * (-1)
            if sync(h):
                print(h, end=" ")
                break
        while True:
            h = heapq.heappop(MinQueue)
            if sync(h):
                print(h)
                break
