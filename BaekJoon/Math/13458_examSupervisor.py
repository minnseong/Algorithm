# BaekJoon 04/14 2022
# 삼성 SW 역량 테스트 기출 문제
# 13458 시험 감독

import sys
import math
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

res = 0

for aa in a:
    aa -= b
    res += 1
    if aa > 0:
        res += (math.ceil(aa/c))

print(res)