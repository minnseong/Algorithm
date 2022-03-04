# BaekJoon 03/04 2022
# 21317 징검다리 건너기

import math

n = int(input())
stone = []
for _ in range(n-1):
    stone.append(list(map(int, input().split())))
k = int(input())

dp = [math.inf] * n
dp[0] = 0
for i in range(1, n):
    if i == 1:
        dp[i] = min(dp[i], stone[i-1][0] + dp[i-1])
    else:
        dp[i] = min(dp[i], stone[i-1][0] + dp[i-1], stone[i-2][1] + dp[i-2])

res = dp[-1]

for i in range(0, n-3):
    tmp = [math.inf] * n
    tmp[0] = 0
    j = 0
    while j < n:
        if j == i: # 슈퍼 점프
            if j != 0:
                if j == 1:
                    tmp[j] = min(tmp[j], stone[j-1][0] + tmp[j-1])
                else:
                    tmp[j] = min(tmp[j], stone[j-1][0] + tmp[j-1], stone[j-2][1] + tmp[j-2])
            s = tmp[j] + k
            tmp[j+3] = s
            j += 4
        elif j == 0: # 첫번째 돌 넘어가기
            j += 1
            pass
        elif j == 1 or j == i + 4: # 두번째 돌이거나 슈퍼점프 다음 돌 
            tmp[j] = min(tmp[j], stone[j-1][0] + tmp[j-1])
            j += 1
        else: # 나머지
            tmp[j] = min(tmp[j], stone[j-1][0] + tmp[j-1], stone[j-2][1] + tmp[j-2])
            j += 1
    res = min(tmp[-1], res)

print(res)