# BaekJoon 03/17 2022
# 9655 돌 게임

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    dp.append(min(dp[i-1]+1, dp[i-3]+1))

if dp[-1] & 1:
    print("SK")
else:
    print("CY")