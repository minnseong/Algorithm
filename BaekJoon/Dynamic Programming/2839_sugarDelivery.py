# BaekJoon 03/16 2022
# 2839 설정 배달

import math

n = int(input())
dp = [math.inf] * (n+1)
dp[0] = 0
if n >= 3: 
    dp[3] = 1
if n >= 5:
    dp[5] = 1

for i in range(6, len(dp)):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1)

if dp[-1] == math.inf:
    print(-1)
else:
    print(dp[-1])