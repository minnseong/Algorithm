# BaekJoon 03/25 2023
# 12865 평범한 배낭

import sys

N, K = map(int, input().split())

bags = []
for _ in range(N):
    bags.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = bags[i-1][0], bags[i-1][1]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp)        