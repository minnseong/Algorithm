# BaekJoon 03/20 2022
# 9095 1,2,3 더하기

n = int(input())

for _ in range(n):
    t = int(input())
    dp = [0] * (t+1)
    dp[0], dp[1] = 1, 1
    for i in range(2, t+1):
        dp[i] += dp[i-1]
        dp[i] += dp[i-2]
        if i >= 3:
            dp[i] += dp[i-3]
    print(dp[-1])