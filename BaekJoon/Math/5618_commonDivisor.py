import sys


def divisor(n, flag):
    div = []
    if flag == 1:
        for i in range(1, (n//2) + 1):
            if n % i == 0:
                div.append(i)

        div.append(n)
        return div
    elif flag == 2:
        for i in range(1, (n//2) + 1):
            if n % i == 0:
                print(i)
        print(n)


N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

minValue = min(num)
num.remove(minValue)
minDivisor = reversed(divisor(minValue, 1))

for m in minDivisor:
    cnt = 0
    for n in num:
        if n % m == 0:
            cnt += 1
    if cnt == len(num):
        ans = m
        divisor(ans, 2)
        break
