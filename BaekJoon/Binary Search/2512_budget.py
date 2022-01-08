# BaekJoon 01/08 2022
# 2512 예산

N = int(input())
request_budget = list(map(int, input().split()))
budget = int(input())

start = 1
end = max(request_budget)

while start <= end:
    mid = (start + end) // 2
    budgetSum = 0
    for b in request_budget:
        if b > mid:
            budgetSum += mid
        else:
            budgetSum += b
    
    if budgetSum > budget:
        end = mid-1
    else:
        start = mid+1

print(end)