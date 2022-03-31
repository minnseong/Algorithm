# BaekJoon 03/31 2022
# 9465 스티커

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    for i in range(1, n):
        if i == 1:
            stickers[0][i] += stickers[1][i-1]
            stickers[1][i] += stickers[0][i-1]
        else:
            stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
            stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2])
    print(max(stickers[0][n-1], stickers[1][n-1]))