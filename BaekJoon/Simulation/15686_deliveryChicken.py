# Programmers 02/28 2023
# 골드5 - 치킨 배달

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

board = list()
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

homes = list()
chickens = list()

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            homes.append((i, j))
        elif board[i][j] == 2:
            chickens.append((i, j))

answer = list()
for combi in list(combinations(chickens, M)):
    tmp_answer = 0
    for h in homes:
        tmp_distance = 1e9
        for c in combi:
            tmp_distance = min(tmp_distance, (abs(h[0]-c[0])+ abs(h[1]-c[1])))
        tmp_answer += tmp_distance
    answer.append(tmp_answer)

print(min(answer))