# BackJoon 03/17 2023
# 골드4 - 부분합

import sys
N, S = map(int, input().split())
num = list(map(int, input().split()))

i, j = 0, 0
sub_sum = 0
result = sys.maxsize

while True:
    if sub_sum >= S:
        result = min(result, j-i)
        sub_sum -= num[i]
        i += 1
    elif j == N:
        break
    else:
        sub_sum += num[j]
        j += 1

if result == sys.maxsize:
    print(0)
else:
    print(result)