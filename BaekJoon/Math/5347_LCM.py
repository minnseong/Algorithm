# BaekJoon 09/11 2021
# 5347 LCM

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    maxV = max(A, B)
    minV = min(A, B)

    n = 2
    tmp = maxV
    while True:
        if maxV % minV == 0:
            print(maxV)
            break
        else:
            maxV = tmp * n
            n += 1
