# Programmers 03/25 2021
# 게임 맵 최단거리
from collections import deque


def solution(maps):
    width = len(maps[0]) - 1
    height = len(maps) - 1
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visit = {(0, 0)}
    queue = deque()
    queue.append((0, 0, 1))

    while queue:
        tmp = queue.popleft()
        y = tmp[0]
        x = tmp[1]
        check = tmp[2]

        if y == height and x == width:
            return check

        for my, mx in move:
            ny = y + my
            nx = x + mx
            set_size = len(visit)
            if 0 <= ny <= height and 0 <= nx <= width and maps[ny][nx] == 1:
                visit.add((ny, nx))
                if set_size != len(visit):
                    queue.append((ny, nx, check + 1))

    return -1

print(solution([[1, 0, 1, 1, 1],
                [1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1],
                [1, 1, 1, 0, 1],
                [0, 0, 0, 0, 1]]))



