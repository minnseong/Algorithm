# Programmers 03/24 2022
# 쿼드압축 후 개수 세기

import copy

def checkQuad(arr, x, y, l):
    sp = arr[x][y]
    for i in range(x, x+l):
        for j in range(y, y+l):
            if sp != arr[i][j]:
                return -1
    return sp    

def splitArr(rg, l):
    return ([[rg[0], rg[1]], [rg[0]+l, rg[1]], [rg[0], rg[1]+l], [rg[0]+l, rg[1]+l]])

def solution(arr):
    answer = [0, 0]

    rg, tmp = [[0,0]], [[0,0]]
    l = len(arr)

    while True:
        rg = copy.deepcopy(tmp)
        if len(rg) == 0:
            break
        tmp = []
        for r in rg:
            c = checkQuad(arr, r[0], r[1], l)
            if c == -1:
                tmp.extend(splitArr(r, l // 2))
            else:
                answer[c] += 1
        l //= 2
    
    return answer

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))
print(solution([[1]]))
print(solution([[1,1],[1,1]]))