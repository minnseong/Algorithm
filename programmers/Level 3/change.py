# Programmers 07/13 2022
# 거스름돈

def solution(n, money):
    dp = [0] * (n+1)
    dp[0] = 1

    for m in money:
        for i in range(m, len(dp)):
            dp[i] = dp[i] + dp[i-m]

    return dp[-1]

print(solution(5, [1,2,5]))