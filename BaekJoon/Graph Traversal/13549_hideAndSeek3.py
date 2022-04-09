# BaekJoon 04/09 2022
# 13549 숨바꼭질3

from collections import deque
n, k = map(int, input().split())

time = [-1] * 100001
visited = [False] * 100001

queue = deque([n])
time[n] = 0
visited[n] = True

while queue:
    if time[k] != -1:
        break

    s = queue.popleft()
    if s*2 <= 100000 and not visited[s*2]:
        time[s*2] = time[s]
        visited[s*2] = True
        queue.appendleft(s*2)
    if s-1 >= 0 and not visited[s-1]:
        time[s-1] = time[s] + 1
        visited[s-1] = True
        queue.append(s-1)
    if s+1 <= 100000 and not visited[s+1]:
        time[s+1] = time[s] + 1
        visited[s+1] = True
        queue.append(s+1)

print(time[k])
