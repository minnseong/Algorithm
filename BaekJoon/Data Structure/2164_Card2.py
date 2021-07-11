from collections import deque


N = int(input())
card = [i+1 for i in range(N)]
queue = deque(card)

while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])