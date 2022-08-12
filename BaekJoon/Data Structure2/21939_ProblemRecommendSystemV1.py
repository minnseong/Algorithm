# BaekJoon 08/12 2022
# 21939 문제 추천 시스템 Version 1 
# 100% Failed

import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_h = []
max_h = []

for _ in range(N):
    num, level = map(int, input().split())
    heapq.heappush(min_h, [level, num])
    heapq.heappush(max_h, [-level, -num])

M = int(input())
solvedSet = set()
for _ in range(M):
    cmd = input().split()
    if cmd[0] == "add":
        heapq.heappush(min_h, [int(cmd[2]), int(cmd[1])])
        heapq.heappush(max_h, [int(cmd[2])*(-1), int(cmd[1])*(-1)])
        # if int(cmd[1]) in solvedSet:
        #     solvedSet.remove(int(cmd[1]))
    elif cmd[0] == "recommend":
        if cmd[1] == '1':
            while True:
                if max_h[0][1]*(-1) in solvedSet:
                    heapq.heappop(max_h)
                else:
                    print(max_h[0][1]*(-1))
                    break
        elif cmd[1] == '-1':
            while True:
                if min_h[0][1] in solvedSet:
                    heapq.heappop(min_h)
                else:
                    print(min_h[0][1])
                    break
    elif cmd[0] == "solved":
        solvedSet.add(int(cmd[1]))

