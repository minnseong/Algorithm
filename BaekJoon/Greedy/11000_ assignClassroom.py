# BaekJoon 10/26 2021
# 11000 강의실 배정

import sys
from queue import PriorityQueue

N = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]
cnt = 0

classes.sort(key=lambda x: x[1])
classes.sort(key=lambda x: x[0])

schedule = PriorityQueue()
for i in range(len(classes)):
    if i == 0:
        schedule.put(classes[i][1])
        cnt += 1
    else:
        tmp = schedule.get()
        if tmp > classes[i][0]:
            schedule.put(classes[i][1])
            schedule.put(tmp)
            cnt += 1
        else:
            tmp = classes[i][1]
            schedule.put(tmp)

print(cnt)
