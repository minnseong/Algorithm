# BaekJoon 09/11 2021
# 1934 최소공배수

T = int(input())


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


for i in range(T):
    A, B = map(int, input().split())
    print(int((A*B)/gcd(A, B)))
