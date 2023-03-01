# BaekJoon 03/01 2023
# 골드5 - 수 고르기

import sys

N, M = map(int, input().split())
numbers = list()

for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()

i = 0
j = 1

answer = sys.maxsize
while i <= j and j < N:
    if numbers[j]-numbers[i] >= M:
        answer = min(answer, numbers[j]-numbers[i])
        i += 1
    else:
        j += 1

print(answer)