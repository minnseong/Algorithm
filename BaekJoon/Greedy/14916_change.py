# BaekJoon 10/07 2021
# 14916 거스름돈

n = int(input())
cnt = 0

fiveCnt = n // 5
rest = n % 5

if n == 1 or n == 3:
    print(-1)
else:
    while True:
        if rest % 2 == 0:
            twoCnt = rest // 2
            print(fiveCnt + twoCnt)
            break
        else:
            rest += 5
            fiveCnt -= 1
