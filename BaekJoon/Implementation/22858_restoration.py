# BaekJoon 02/01 2022
# 22858 원상 복구 (small)

import sys

N, K = map(int, input().split())
s = list(map(int, sys.stdin.readline().split()))
d = list(map(int, sys.stdin.readline().split()))

for _ in range(K):
    rst = [0] * len(d)
    for i in range(len(d)):
        rst[d[i]-1] = s[i]
    s = rst

print(*rst)