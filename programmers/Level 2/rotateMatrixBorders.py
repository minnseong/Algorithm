# Programmers 01/08 2022
# 행렬 테두리 회전하기

# return : [회전한 행렬, 그 중 최솟값]
def rotateBorder(matrix, q):
    y1, x1, y2, x2 = int(q[0])-1, int(q[1])-1, int(q[2])-1, int(q[3])-1
    
    # 위
    prev = matrix[y1][x2]
    matrix[y1][x1+1:x2+1] = matrix[y1][x1:x2]
    minNum = min(matrix[y1][x1+1:x2+1])

    # 오
    prv = matrix[y2][x2]
    for y in range(y2, y1, -1):
        matrix[y][x2] = matrix[y-1][x2]
        minNum = min(minNum, matrix[y][x2])
    matrix[y1+1][x2] = prev
    minNum = min(minNum, matrix[y1+1][x2])

    # 아래
    prev = matrix[y2][x1]
    matrix[y2][x1:x2] = matrix[y2][x1+1:x2+1]
    minNum2 = min(matrix[y2][x1:x2])
    minNum = min(minNum, minNum2)
    matrix[y2][x2-1] = prv
    minNum = min(minNum, matrix[y2][x2-1])

    # 오
    for y in range(y1, y2):
        matrix[y][x1] = matrix[y+1][x1]
        minNum = min(minNum, matrix[y][x1])
    matrix[y2-1][x1] = prev
    minNum = min(minNum, matrix[y2-1][x1])

    return [matrix, minNum]

def solution(rows, columns, queries):
    answer = []
    matrix = []

    for r in range(1, rows+1):
        tmp = []
        for c in range(1, columns+1):
            tmp.append((r-1)*columns + c)
        matrix.append(tmp)

    for q in queries:
        matrix, num = rotateBorder(matrix, q)
        answer.append(num)

    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
# print(solution(100,97,[[1,1,100,97]]))