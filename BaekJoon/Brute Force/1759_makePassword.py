# BaekJoon 05/06 2022
# 1759 암호 만들기

from itertools import combinations
import sys
input = sys.stdin.readline

L, C = map(int, input().split())
ch = sorted(input().split())
combi = combinations(ch, L)

for c in combi:
    vowelCnt = len({'a', 'i', 'o', 'e', 'u'} & set(c))
    if vowelCnt >= 1 and L - vowelCnt >= 2:
        print(''.join(list(c)))