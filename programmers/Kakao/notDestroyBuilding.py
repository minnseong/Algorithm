# Programmers 07/10 2022
# KaKao 파괴되지 않은 건물

def solution(board, skill):
    answer = 0
    prefixSum = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            prefixSum[r1][c1] -= degree
            prefixSum[r1][c2+1] += degree
            prefixSum[r2+1][c1] += degree
            prefixSum[r2+1][c2+1] -= degree
        elif type == 2:
            prefixSum[r1][c1] += degree
            prefixSum[r1][c2+1] -= degree
            prefixSum[r2+1][c1] -= degree
            prefixSum[r2+1][c2+1] += degree

    for i in range(len(prefixSum)-1):
        for j in range(len(prefixSum[0])-1):
            prefixSum[i][j+1] += prefixSum[i][j]

    for i in range(len(prefixSum[0])-1):
        for j in range(len(prefixSum)-1):
            prefixSum[j+1][i] += prefixSum[j][i]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] + prefixSum[i][j] > 0:
                answer += 1
    
    return answer

# print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))

''' 시간초과
def doSkill(type, rg1, rg2, degree, board):
    for i in range(rg1[0], rg2[0]):
        for j in range(rg1[1], rg2[1]):
            if type == 1:
                board[i][j] -= degree
            else:
                board[i][j] += degree
            
def solution(board, skill):
    answer = 0

    for s in skill:
        type, rg1, rg2, degree = s[0], [s[1], s[2]], [s[3]+1, s[4]+1], s[5]
        doSkill(type, rg1, rg2, degree, board)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1

    return answer
'''

