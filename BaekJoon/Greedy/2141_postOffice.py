# BaekJoon 10/28 2021
# 2141 우체국

N = int(input())
X = []
A = []
loc = 0
res = 0

for _ in range(N):
    xx, aa = map(int, input().split())
    X.append(xx)
    A.append(aa)

for i in range(N):
    tmp = 0
    for j in range(N):
        tmp += abs(X[i] - X[j]) * A[j]
    if tmp < loc or loc == 0:
        loc = tmp
        res = i

print(res+1)
