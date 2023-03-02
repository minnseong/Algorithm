# BaekJoon 03/02 2023
# 골드4 - 세 수의 합

from itertools import combinations_with_replacement
import sys

N = int(input())

numbers = list()
for _ in range(N):
    numbers.append(int(input()))

two = set()
numbers.sort()
for combi in combinations_with_replacement(numbers, 2):
    two.add(sum(combi))

for i in range(N-1, -1, -1):
    for j in range(i):
        if (numbers[i]-numbers[j]) in two:
            print(numbers[i])
            sys.exit()

"""
numbers_set = set(numbers)

answer = 0
for combi in combinations(numbers, 3):
    sum_ = sum(combi)
    if sum_ in numbers_set:
        answer = max(answer, sum_)

print(answer)
"""