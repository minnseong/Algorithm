# BaekJoon 09/10 2021
# 21920 서로소 평균

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


N = int(input())
arr = list(map(int, input().split()))
X = int(input())

RParr = []

for i in arr:
    if gcd(X, i) == 1:
        RParr.append(i)

print(sum(RParr)/len(RParr))
