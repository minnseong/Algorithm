# BaekJoon 11/08 2021
# 18511 큰 수 구성하기

from itertools import product

N, K = map(int, input().split())
arr = list(map(str, input().split()))
numArr = []
res = 0


for j in range(1, len(str(N))+1):
    for i in product(arr, repeat=j):
        numArr.append(int("".join(i)))

for n in numArr:
    if N >= n and n >= res:
        res = n

print(res)
