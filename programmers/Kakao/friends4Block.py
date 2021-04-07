# Programmers 04/04 2021
# KaKao 프렌즈4블록

def solution(m, n, board):
    answer = 0
    newboard = []
    trash = 0

    for i in board:
        tmp = []
        for j in range(len(i)):
            tmp.append(i[j])
        newboard.append(tmp)

    while True:
        same = set()

        for i in range(1, m):
            for j in range(1, n):
                if newboard[i-1][j-1] == newboard[i-1][j] == newboard[i][j-1] == newboard[i][j]:
                    same.add((i-1, j-1))
                    same.add((i-1, j))
                    same.add((i, j-1))
                    same.add((i, j))

        if len(same) == 0:
            break

        for i, j in same:
            newboard[i][j] = 0
            answer += 1

        rotate = []
        for i in range(0, n):
            tmp = []
            for j in range(m-1, -1, -1):
                tmp.append(newboard[j][i])
            rotate.append(tmp)

        for i in rotate:
            while 0 in i:
                i.remove(0)

        #print(rotate)
        for i in rotate:
            while len(i) != m:
                i.append(trash)
                trash += 1

        rerotate = []
        for i in range(m-1, -1, -1):
            tmp = []
            for j in range(0, n):
                tmp.append(rotate[j][i])
            rerotate.append(tmp)

        #print(rotate)
        print(rerotate)

        newboard = rerotate

    return answer

print(solution(4,5,["CCBDE",
                    "AAADE",
                    "AAABF",
                    "CCBBF"]))

