# BackJoon 09/10 2021
# 2609 최대공약수와 최소공배수

N, M = map(int, input().split())

maxNum = max(N, M)
minNum = min(N, M)

while 1:
    temp = maxNum % minNum
    maxNum = minNum
    minNum = temp

    if temp != 0:
        continue
    else:
        break

icm = int(N*M/maxNum)
print(maxNum)
print(icm)
