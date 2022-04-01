# BaekJoon 04/01 2022
# 삼성 SW 역량 테스트 기출 문제
# 14501 퇴사

n = int(input())
consultingTime = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n):
    if i+consultingTime[i][0] <= n:
        for j in range(i+consultingTime[i][0], n+1):
            dp[j] = max(dp[i+consultingTime[i][0]], dp[i]+consultingTime[i][1])

print(dp[-1])

'''
skiped = [False for _ in range(n)]
maxResult = 0

for i in range(n):
    if skiped[i]:
        continue
    
    j = i
    tmp = 0
    while j < n:
        if j + consultingTime[j][0] <= n:
            tmp += consultingTime[j][1]
            skiped[j] = True
            j += (consultingTime[j][0])
        else:
            break
    maxResult = max(maxResult, tmp)

print(maxResult)
'''