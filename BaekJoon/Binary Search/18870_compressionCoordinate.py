# BaekJoon 03/02 2023
# 실버2 - 좌표 압축

import copy
import bisect

N = int(input())
numbers = list(map(int, input().split()))

tmp_numbers = copy.deepcopy(numbers)
tmp_numbers = list(set(tmp_numbers))
tmp_numbers.sort()

for n in numbers:
    print(bisect.bisect_left(tmp_numbers, n), end=" ")