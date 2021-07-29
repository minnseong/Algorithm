import sys
from queue import PriorityQueue

T = int(sys.stdin.readline())
ans = []

for _ in range(T):
    k = int(sys.stdin.readline())
    MaxQueue = PriorityQueue()
    MinQueue = PriorityQueue()
    cnt = 0

    for _ in range(k):
        cmd = list(sys.stdin.readline().split())
        if cmd[0] == "I":
            MaxQueue.put(int(cmd[1]) * (-1))
            MinQueue.put(int(cmd[1]))
            cnt += 1
        else:
            if cnt == 0:
                continue
            else:
                if cmd[1] == '1':
                    MaxQueue.get()
                else:
                    MinQueue.get()
            cnt -= 1

    if cnt == 0:
        ans.append("EMPTY")
    elif cnt == 1:
        ans.append(MinQueue.get())
    else:
        ans.append(str(MaxQueue.get() * (-1)) + " " + str(MinQueue.get()))

for a in ans:
    print(a)