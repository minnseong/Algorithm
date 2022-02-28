# BaekJoon 02/28 2022
# 2798 블랙잭

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

comb = combinations(cards, 3)
for c in comb:
    if M >= sum(c) and result <= sum(c):
        result = sum(c)

print(result)