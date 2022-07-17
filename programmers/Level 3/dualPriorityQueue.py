# Programmers 07/17 2022
# 이중우선순위큐

import heapq

def solution(operations):
    answer = []

    maxheap = []
    minheap = []

    maxheapCnt = 0
    minheapCnt = 0
    dataCnt = 0
    for o in operations:
        cmd, data = o.split(" ")
        if cmd == "I":
            heapq.heappush(maxheap, int(data)*(-1))
            heapq.heappush(minheap, int(data))
            maxheapCnt += 1
            minheapCnt += 1
            dataCnt += 1
        else:
            if minheapCnt + maxheapCnt > 0:
                if data == "1":
                    maxheapCnt -= 1
                    heapq.heappop(maxheap)
                else:
                    minheapCnt -=1
                    heapq.heappop(minheap)

                if maxheapCnt + minheapCnt == dataCnt:
                        maxheap, minheap = list(), list()
                        maxheapCnt, minheapCnt, dataCnt = 0, 0, 0

    if minheapCnt + maxheapCnt == 0:
        return [0, 0]
    return [maxheap[0]*(-1), minheap[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))