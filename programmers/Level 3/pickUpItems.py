# Programmers 07/14 2022
# 아이템 줍기
# 합계: 57.9 / 100.0

def fillBoard(board, point):
    for i in range(point[1], point[3]+1):
        for j in range(point[0], point[2]+1):
            board[i][j] = 1

def check(y, x, board):
    if 0 <= y+1 < 51 and 0 <= x+1 < 51 and board[y+1][x+1] == 0:
        return True
    if 0 <= y+1 < 51 and 0 <= x-1 < 51 and board[y+1][x-1] == 0:
        return True
    if 0 <= y-1 < 51 and 0 <= x+1 < 51 and board[y-1][x+1] == 0:
        return True
    if 0 <= y-1 < 51 and 0 <= x-1 < 51 and board[y-1][x-1] == 0:
        return True

    if 0 <= y+1 < 51 and 0 <= x < 51 and board[y+1][x] == 0:
        return True
    if 0 <= y < 51 and 0 <= x-1 < 51 and board[y][x-1] == 0:
        return True
    if 0 <= y-1 < 51 and 0 <= x < 51 and board[y-1][x] == 0:
        return True
    if 0 <= y < 51 and 0 <= x+1 < 51 and board[y][x+1] == 0:
        return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    board = [[0] * 51 for _ in range(51)]
    for r in rectangle:
        fillBoard(board, r)

    dir = [[0,1], [1,0], [-1,0], [0,-1]]
    visited = [[False] * 51 for i in range(51)]

    stack = [[characterY, characterX]]

    distance = -1
    compareDistance = 0

    while stack:
        y, x = stack.pop()
        visited[y][x] = True
        board[y][x] = 4
        distance += 1

        if y == itemY and x == itemX:
            board[y][x] = 8
            compareDistance = distance

        for d in dir:
            dy, dx = y+d[0], x+d[1]

            if 0 <= dy < 51 and 0 <= dx < 51 and board[dy][dx] and not visited[dy][dx]:
                if check(dy, dx, board):
                    stack.append([dy, dx])   
                    break 
    # for b in board:
    #     print(*b)
    print(distance+1)
    return min(distance+1-compareDistance, compareDistance)

# print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
# print()
# print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9,7,6,1))
# print()
# print(solution([[1,1,5,7]], 1, 1, 4, 7))
# print()
# print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
# print()
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))