# BaekJoon 03/14 2022
# 1463 1로 만들기

x = int(input())

dp = [0] * (x+1)

for i in range(2, len(dp)):
    dp[i] = dp[i-1] + 1

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[-1])

# 0 0 1

''' 
혹시나 bfs 사용해봤지만 - 시간초과

from collections import deque

x = int(input())

queue = deque([[x, 0]])

while queue:
    value, times = queue.popleft()

    if value == 1:
        print(times)
        break
    
    if value % 3 == 0:
        queue.append([value/3 , times+1])
    if value % 2 == 0:
        queue.append([value/2 , times+1])
    queue.append([value-1, times+1])
'''