# Programmers 03/01 2023
# 실버4 - 수 찾기

import bisect

N = int(input())
numbers = list(map(int, input().split()))

M = int(input())
find_numbers= list(map(int, input().split()))

numbers.sort()

for fn in find_numbers:
    index = bisect.bisect_right(numbers, fn) - bisect.bisect_left(numbers, fn)
    if index == 0:
        print(0)
    else:
        print(1)
    