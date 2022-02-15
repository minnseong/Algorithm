# BaekJoon 02/15 2022
# 1764 듣보잡

''''
    set의 교집합 합집합 차집합 구하기.

    & : 교집합
    | : 합집합
    - : 차집합
'''
import sys

N, M = map(int, input().split())

arr1 = set()
arr2 = set()

for _ in range(N):
    arr1.add(sys.stdin.readline().strip())

for _ in range(M):
    arr2.add(sys.stdin.readline().strip())

result = sorted(list(arr1 & arr2))

print(len(result))
for r in result:
    print(r)