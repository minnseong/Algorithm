# BaekJoon 04/08 2022
# 13549 숨바꼭질3

from collections import deque

n, k = map(int, input().split())

visited = [False] * 100001
time = [-1] * 100001
queue = deque()
queue.append(n)
visited[n] = True
time[n] = 0

while queue:
    q = queue.popleft()

    if q * 2 <= 10001 and not visited[q*2]:
        time[q*2] = time[q]
        visited[q*2] = True
        queue.appendleft(q*2)
    if q + 1 <= 10001 and not visited[q+1]:
        time[q+1] = time[q]+1
        visited[q+1] = True
        queue.append(q+1)
    if q - 1 >= 0 and not visited[q-1]:
        time[q-1] = time[q]+1
        visited[q-1] = True
        queue.append(q-1)

print(time[k])