# BaekJoon 03/30 2022
# 삼성 SW 역량 테스트 기출 문제
# 14889 스타크와 링크

import sys
from itertools import combinations, permutations
input = sys.stdin.readline

n = int(input())
synergy = [list(map(int, input().split())) for _ in range(n)]

idx = [i for i in range(1, n+1)]
combi = list(combinations(idx, n//2))
res = []

for i in range(len(combi) // 2):
    sn_start = list(permutations(combi[i], 2))
    sn_link = list(permutations(combi[len(combi)-1-i], 2))
    
    sum_start, sum_link = 0, 0
    for s in sn_start:
        sum_start += synergy[s[0]-1][s[1]-1]
    for s in sn_link:
        sum_link += synergy[s[0]-1][s[1]-1]
    
    res.append(abs(sum_start-sum_link))

print(min(res))
