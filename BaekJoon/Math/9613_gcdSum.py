# BaekJoon 09/12 2021
# 9613 GCD 합
from itertools import combinations


def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)


t = int(input())

for i in range(t):
    tc = list(map(int, input().split()))
    tc.pop(0)
    sum = 0
    combi = list(combinations(tc, 2))
    for c in combi:
        sum += GCD(c[0], c[1])
    print(sum)
