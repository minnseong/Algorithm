# BaekJoon 06/03 2022
# 2285 우체국

import sys
sys = sys.stdin.readline;

n = int(input())
country = [] 
total = 0
for _ in range(n):
    c = list(map(int, input().split()))
    total += c[1]
    country.append(c)

country.sort(key=lambda x : x[0])
cnt = 0
for c in country:
    cnt += c[1]
    if cnt >= total / 2:
        print(c[0])
        break