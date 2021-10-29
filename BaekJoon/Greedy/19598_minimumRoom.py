# BaekJoon 10/29 2021
# 19598 최소 회의실 개수

import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
conf = []
room = PriorityQueue()

for _ in range(N):
    conf.append(list(map(int, sys.stdin.readline().split())))

conf.sort(key=lambda x: x[0])

for c in range(len(conf)):
    if room.empty():
        room.put(conf[c][1])
    else:
        tmp = room.get()
        if conf[c][0] >= tmp:
            room.put(conf[c][1])
        else:
            room.put(conf[c][1])
            room.put(tmp)

print(room.qsize())
