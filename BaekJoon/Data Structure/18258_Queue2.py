from collections import deque
import sys

def isEmpty():
    if len(queue) == 0:
        return 1
    else:
        return 0


N = int(sys.stdin.readline())
queue = deque()

for i in range(N):
    c = sys.stdin.readline().split()

    if c[0] == 'push':
        queue.append(c[1])
    elif c[0] == 'pop':
        if isEmpty():
            print(-1)
        else:
            print(queue.popleft())
    elif c[0] == 'size':
        print(len(queue))
    elif c[0] == 'empty':
        print(isEmpty())
    elif c[0] == 'front':
        if isEmpty():
            print(-1)
        else:
            print(queue[0])
    elif c[0] == 'back':
        if isEmpty():
            print(-1)
        else:
            print(queue[-1])