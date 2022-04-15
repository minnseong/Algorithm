# BaekJoon 04/15 2022
# 삼성 SW 역량 테스트 기출 문제
# 21608 상어 초등학교

import sys
input = sys.stdin.readline

n = int(input())
order = []
like_dic = dict()
board = [[0] * n for _ in range(n)]
result = 0

for _ in range(n*n):
    tmp = list(map(int, input().split()))
    order.append(tmp[0])
    like_dic[tmp[0]] = tmp[1:]

def getIdjacency(x, y, id):
    res = [x, y, 0, 0] #인접한 사람 중 좋아하는 사람의 수, 인접한 칸중 비어잇는 자리의 수
    dir = [[0,1], [1,0], [-1,0], [0,-1]]
    for d in dir:
        dx = x + d[0]
        dy = y + d[1]
        if 0 <= dx < n and 0 <= dy < n:
            if board[dx][dy] in like_dic[id]:
                res[2] += 1
            if board[dx][dy] == 0:
                res[3] += 1

    return res

def selectSeat(id):
    canSitSeat = []
    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                canSitSeat.append(getIdjacency(i, j, id))
    
    canSitSeat.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))
    return canSitSeat[0]

for o in order:
    seat = selectSeat(o)
    board[seat[0]][seat[1]] = o

for i in range(n):
    for j in range(n):
        info = getIdjacency(i, j, board[i][j])
        if info[2] == 1:
            result += 1
        elif info[2] == 2:
            result += 10
        elif info[2] == 3:
            result += 100
        elif info[2] == 4:
            result += 1000

print(result)