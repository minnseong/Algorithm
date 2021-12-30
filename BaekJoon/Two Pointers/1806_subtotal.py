# BackJoon 12/30 2021
# 1806 부분합

N, S = map(int, input().split())
num = list(map(int, input().split()))

i, j = 0, 1
minLength = N
subSum = [num[i], 1]

while i != j:
    if j < N and subSum[0] < S:
        subSum[0] += num[j]
        subSum[1] += 1
        j += 1

    else:
        if subSum[0] >= S and minLength > subSum[1]:
            minLength = subSum[1]
            if minLength == 1:
                break
        subSum[0] -= num[i]
        subSum[1] -= 1
        i += 1
    
    if i == 0 and j == N and subSum[0] < S:
        minLength = 0
        break

print(minLength)