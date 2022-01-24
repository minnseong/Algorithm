# BaekJoon 01/24 2022
# 2578 빙고

import sys

bb = [list(map(int, input().split())) for i in range(5)] # 빙고판
call = [list(map(int, input().split())) for i in range(5)]

bbDict = dict()
column = dict()
row = dict()
cross = {1: 0, 2: 0}
bingo = 0
cnt = 0

for i in range(len(bb)):
    for j in range(len(bb[0])):
        bbDict[bb[i][j]] = [i,j]

for i in range(5):
    column[i] = 0
    row[i] = 0

for i in range(len(call)):
    for j in range(len(call[0])):
        num = call[i][j]
        row[bbDict[num][0]] += 1
        column[bbDict[num][1]] += 1
        cnt += 1

        if row[bbDict[num][0]] == 5:
            bingo += 1
        if column[bbDict[num][1]] == 5:
            bingo += 1
        if bbDict[num] in [[0,0], [1,1], [2,2], [3,3], [4,4]]:
            cross[1] += 1
            if cross[1] == 5:
                bingo += 1
        if bbDict[num] in [[0,4], [1,3], [2,2], [3,1], [4,0]]:
            cross[2] += 1
            if cross[2] == 5:
                bingo += 1     

        if bingo >= 3:
            print(cnt)
            sys.exit(0)
    
        

# 00 01 02 03 04
# 10 11 12 13 14
# 20 21 22 23 24
# 30 31 32 33 34
# 40 41 42 43 44