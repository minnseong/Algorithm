# BaekJoon 09/11 2022
# 12865 평범한 배낭

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = items[i-1][0]
        v = items[i-1][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], v+dp[i-1][j-w])

print(dp[N][K])