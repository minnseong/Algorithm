# Programmers 05/28 2022
# 2022 라인 인턴 코딩 테스트 Q2

def solution(n, times):
    dp = [1e9] * (n+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(1, len(times)+1):
        for j in range(i, len(dp), i):
            if i == j:
                continue
            dp[j] = min(dp[j-i] + times[i-1], dp[j])

    dp[-1] = min(dp[-1], dp[-2]+times[0])
    return dp[-1]

print(solution(4, [2,3]))
print(solution(5, [2,4,5]))
print(solution(6, [1,2,3]))

print(solution(4, [10,4]))
print(solution(9, [10, 11, 12,13])) # 53