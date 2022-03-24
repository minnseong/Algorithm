# Programmers 03/24 2022
# 등굣길

def solution(m, n, puddles):
    m, n = n, m
    board = [[0] * m for _ in range(n)]

    for p in puddles:
        board[p[0]-1][p[1]-1] = -1
    
    for i in range(m):
        if board[0][i] == -1:
            break
        board[0][i] = 1
    
    for i in range(n):
        if board[i][0] == -1:
            break
        board[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] != -1:
                if board[i-1][j] != -1:
                    board[i][j] += board[i-1][j]
                if board[i][j-1] != -1:
                    board[i][j] += board[i][j-1]
    
    return (board[n-1][m-1] % 1000000007)

print(solution(4,3,[[2,2]]))