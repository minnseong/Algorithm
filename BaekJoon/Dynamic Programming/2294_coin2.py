# BaekJoon 03/10 2022
# 2294 동전 2

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
coin.sort()

dp = [10001] * (k+1)
dp[0] = 0

for i in range(len(coin)):
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j-coin[i]] + 1)

if dp[-1] == 10001:
    print(-1)
else:
    print(dp[-1])