# Programmers 05/02 2022
# 자물쇠와 열쇠

def rotate(key):
    tmp = [[0] * len(key[0]) for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            tmp[i][j] = key[j][len(key)-1-i]
    return tmp

def check(board, key, lock_len, startIdx):
    flag = True
    for i in range(startIdx[0], startIdx[0]+len(key)):
        for j in range(startIdx[1], startIdx[1]+len(key)):   
            board[i][j] += key[i-startIdx[0]][j-startIdx[1]]

    for i in range(lock_len):
        for j in range(lock_len):
            if board[i+lock_len][j+lock_len] != 1:
                flag = False
                break

    for i in range(startIdx[0], startIdx[0]+len(key)):
        for j in range(startIdx[1], startIdx[1]+len(key)):   
            board[i][j] -= key[i-startIdx[0]][j-startIdx[1]]

    return flag
    

def solution(key, lock):
    answer = True
    lock_len = len(lock)
   
    board = [[0] * (len(lock)*3) for _ in range(len(lock)*3)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            board[i+len(lock)][j+len(lock)] = lock[i][j]

    for i in range(len(board)-len(lock)):
        for j in range(len(board)-len(lock)):
            for _ in range(4):
                key = rotate(key)
                if check(board, key, lock_len, [i, j]):
                    return True
    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))