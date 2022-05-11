# Programmers 05/11 2022
# 경주로 건설
# 테스트 25 실패, 나머지 통과

from collections import deque

def solution(board):

    length = len(board)
    queue = deque()
    dir = [[1,0], [-1,0], [0,1], [0,-1]]
    costs = [[0] * length for _ in range(length)]

    while queue:
        x, y, prevD, cost = queue.popleft()

        for d in dir:
            dx, dy = x+d[0], y+d[1]
            if 0 <= dx < length and 0 <= dy < length and not board[dx][dy]:
                if dx == 0 and dy == 0:
                    continue

                if x == 0 and y == 0:
                    plusCost = 100
                else:
                    if prevD[0] == d[0] and prevD[1] == d[1]:
                        plusCost = 100
                    else:
                        plusCost = 600

                if costs[dx][dy] == 0:
                    queue.append([dx,dy,d,cost+plusCost])
                    costs[dx][dy] = cost+plusCost
                elif costs[dx][dy] >= cost+plusCost:
                    queue.append([dx,dy,d,cost+plusCost])
                    costs[dx][dy] = cost+plusCost  

    return costs[-1][-1]

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 1, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
