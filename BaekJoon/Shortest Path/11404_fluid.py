# BaekJoon 03/08 2023
# 골드4 - 플로이드

import sys
n = int(input())
m = int(input())

table = [[1e9] * (n+1) for _ in range(n+1)]

for _ in range(m):
    i, j, cost = map(int, sys.stdin.readline().split())
    table[i][j] = min(table[i][j], cost)

for i in range(n+1):
    table[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if table[i][j] > table[i][k]+table[k][j]:
                table[i][j] = table[i][k]+table[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if table[i][j] == 1e9:
            print(0, end=" ")
        else:
            print(table[i][j], end=" ")
    print()
