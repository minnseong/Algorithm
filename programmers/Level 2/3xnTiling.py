# Programmers 08/03 2022
# 3 x n 타일링

def solution(n):
    dp = [0] * (n+1)

    dp[0] = 1
    dp[2] = 3

    if n <= 2:
        return dp[n]
        
    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 4 - dp[i-4]

    return dp[-1] % 1000000007

print(solution(4))


# n = 0 -> 0
# n = 2 -> 3
# n = 4 -> 11
# n = 6 -> 41