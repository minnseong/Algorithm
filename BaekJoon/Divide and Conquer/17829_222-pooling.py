# BaekJoon 11/02 2021
# 17829 222-풀링

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
newMatrix = []


def get2th(x, y, arr):
    tmp = []
    for i in range(x, x+2):
        for j in range(y, y+2):
            tmp.append(arr[i][j])

    tmp.sort()
    return tmp[2]


while len(matrix) >= 2:
    newMatrix = []
    for i in range(0, len(matrix[0]), 2):
        row = []
        for j in range(0, len(matrix), 2):
            row.append(get2th(i, j, matrix))
        newMatrix.append(row)

    matrix = newMatrix

print(newMatrix[0][0])
