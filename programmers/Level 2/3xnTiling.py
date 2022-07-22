# Programmers 07/22 2022
# 3 x n 타일링

def solution(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    tmp = 0

    for i in range(2, n + 1, 2):
        dp[i] = (dp[i - 2] * 3) + (tmp * 2)
        tmp += dp[i - 2]

    return dp[n] % 1000000007