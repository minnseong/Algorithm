# Programmers 07/03 2022
# 2022 Dev-Matching: 웹 백엔드 개발자(상반기)-2
# 30

def solution(rows, columns, lands):
    maps = [[0] * columns for _ in range(rows)]
    answer = []
    for i in range(rows):
        for j in range(columns):
            if i == 0 or j == 0 or i == rows-1 or j == columns-1:
                maps[i][j] = 1

    for l in lands:
        maps[l[0]-1][l[1]-1] = 2

    dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
    visited = [[False] * columns for _ in range(rows)]

    for i in range(rows):
        for j in range(columns):
            if (i == 1 or j == 1 or i == rows-2 or j == columns-2) and (i != 0 and j != 0 and i != rows-1 and j != columns-1):
                if maps[i][j] == 0:
                    stack = [[i, j]]
                    while stack:
                        x, y = stack.pop()
                        visited[x][y] = True
                        maps[x][y] = 1

                        for d in dir:
                            dx, dy = x+d[0], y+d[1]
                            if 0 <= dx < rows and 0 <= dy < columns and not visited[dx][dy]:
                                if maps[dx][dy] == 0:
                                    stack.append([dx, dy])
    
    visitedd = [[False] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            cnt = 0
            if maps[i][j] == 0 and not visitedd[i][j]:
                stack = [[i, j]]
                while stack:
                    x, y = stack.pop()
                    visitedd[x][y] = True
                    cnt += 1

                    for d in dir:
                        dx, dy = x+d[0], y+d[1]
                        if 0 <= dx < rows and 0 <= dy < columns and not visitedd[dx][dy]:
                            if maps[dx][dy] == 0:
                                stack.append([dx, dy])
            
            if cnt >=1:
                answer.append(cnt)

    if answer:
        return [min(answer), max(answer)]
    else:
        return [-1, -1]

print(solution(5, 10, [[2,2], [2,5], [4,5], [4,6], [4,4], [4,3], [4,2], [3,2]]))
# print(solution(9, 7, [[2,2], [2,3], [2,5], [3,2],[3,4], [3,5], [3,6],[4,3], [4,6],[5,2],[5,5],[6,2],[6,3],[6,4],[6,6],[7,2],[7,6],[8,3],[8,4],[8,5]]))