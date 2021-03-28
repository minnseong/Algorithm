# Programmers 03/25 2021
# 게임 맵 최단거리

def solution(maps):
    width = len(maps[0]) - 1
    height = len(maps) - 1
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visit = [(0, 0)]
    queue = [(0, 0, 1)]

#    if maps[-1][-2] == 0 and maps[-2][-1] == 0:
#       return -1

    while queue:
        tmp = queue.pop(0)
        y = tmp[0]
        x = tmp[1]
        check = tmp[2]

        for my, mx in move:
            ny = y + my
            nx = x + mx
            if 0 <= ny <= height and 0 <= nx <= width and maps[ny][nx] == 1 and (ny, nx) not in visit:
                queue.append((ny, nx, check+1))
                visit.append((ny, nx))

                if ny == height and nx == width:
                    return check + 1

    return -1


print(solution([[1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1]]))

