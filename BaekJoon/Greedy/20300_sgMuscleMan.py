# BaekJoon 10/12 2021
# 20300 서강근육맨

N = int(input())
loss = list(map(int, input().split()))
loss.sort()

if N & 1:
    min = loss[-1]
    loss.pop()
    for i in range(len(loss)):
        if min < loss[i] + loss[-(1+i)]:
            min = loss[i] + loss[-(1+i)]
else:
    min = -1
    for i in range(N):
        if min < loss[i] + loss[-(1+i)]:
            min = loss[i] + loss[-(1+i)]

print(min)
