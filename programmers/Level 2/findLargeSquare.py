# Programmers 01/20 2022
# 가장 큰 정사각형 찾기

def solution(board):
    answer = 0

    for x in range(1, len(board)):
        for y in range(1, len(board[0])):
            if board[x][y] == 1:
                board[x][y] = board[x][y] + min(board[x-1][y], board[x][y-1], board[x-1][y-1])

    for b in board:
        ans = max(b)
        if ans > answer:
            answer = ans

    return answer**2

print(solution([[0,0,1,1],[1,1,1,1]]))

''' 
처음 작성한 코드 
- 한 좌표에 따라 bfs로 각 좌표의 값을 계산하려 했으나 무한 루프 및 정확한 값 얻기 실패
- 다른 사람의 코드를 참고하여 dynamic programming 적용

def bfs(board, loc):
    dir = [[0, 1], [1, 0], [1, 1]]
    x, y = loc[0], loc[1]
    flag = True

    dxy = []
    for d in dir:
        dx = x + d[0]
        dy = y + d[1]
        dxy.append([dx, dy])

        if not (0 <= dx < len(board) and 0 <= dy < len(board[0])) or board[dx][dy] == 0:
            flag = False
            break
    
    return flag, dxy   

def solution(board):
    answer = 1

    for x in range(len(board)):
        for y in range(len(board[0])):
            cnt = 1
            if board[x][y] == 1:
                isSquare, xy = bfs(board, [x, y])
                while isSquare:
                    tmpxy = []
                    for xxyy in xy:
                        isSquare, txy = bfs(board, xxyy)
                        tmpxy.extend(txy)
                        if not isSquare:
                            break
                    xxyy = tmpxy

                    cnt += 1
            
            if cnt**2 > answer:
                answer = cnt**2

    return answer
'''