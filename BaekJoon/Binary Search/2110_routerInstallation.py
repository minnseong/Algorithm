# BaekJoon 03/01 2023
# 골드4 - 공유기 설치

import sys

N, C = map(int, input().split())
home = [int(sys.stdin.readline()) for _ in range(N)]
home.sort()

start, end = 0, home[-1]-home[0]

answer = 0
while start <= end:
    mid = (start+end) // 2

    cur = home[0]
    cnt = 1
    for i in range(1, N):
        if home[i]-cur >= mid:
            cnt += 1
            cur = home[i]
    
    if cnt >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)