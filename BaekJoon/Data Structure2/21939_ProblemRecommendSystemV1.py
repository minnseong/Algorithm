# BaekJoon 08/13 2022
# 21939 문제 추천 시스템 Version 1 

import sys
import heapq
input = sys.stdin.readline

N = int(input())
min_h = []
max_h = []
dic = dict()

for _ in range(N):
    num, level = map(int, input().split())
    heapq.heappush(min_h, [level, num])
    heapq.heappush(max_h, [-level, -num])
    dic[num] = False

M = int(input())
for _ in range(M):
    cmd = input().strip().split()
    if cmd[0] == "recommend":
        if cmd[1] == '1':
            while dic[-max_h[0][1]]:
                heapq.heappop(max_h)
            print(max_h[0][1] * (-1))
        else:
            while dic[min_h[0][1]]:
                heapq.heappop(min_h)
            print(min_h[0][1])
    elif cmd[0] == "add":
        while dic[-max_h[0][1]]:
            heapq.heappop(max_h)
        while dic[min_h[0][1]]:
            heapq.heappop(min_h)
        dic[int(cmd[1])] = False
        heapq.heappush(min_h, [int(cmd[2]), int(cmd[1])])
        heapq.heappush(max_h, [-int(cmd[2]), -int(cmd[1])])
    else:
        dic[int(cmd[1])] = True