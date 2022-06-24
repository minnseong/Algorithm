# Programmers 06/24 2022
# 멀리 뛰기

def solution(n):
    dp = [0] * (n+1)
    dp[1] = 1
    
    if n == 1:
        return 1
    else:
        dp[2] = 2
        for i in range(2, n+1):
            if i == 2:
                continue
            dp[i] = dp[i-2] + dp[i-1]

    return dp[-1] % 1234567

print(solution(10))
