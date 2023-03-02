# BaekJoon 03/02 2023
# 실버4 - 숫자 카드 2

import bisect

N = int(input())
numbers = list(map(int, input().split()))

M = int(input())
find_numbers= list(map(int, input().split()))

numbers.sort()

for fn in find_numbers:
    print(bisect.bisect_right(numbers, fn) - bisect.bisect_left(numbers, fn), end=" ")