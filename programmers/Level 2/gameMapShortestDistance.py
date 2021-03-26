# Programmers 03/25 2021
# 게임 맵 최단거리
def solution(maps):
    answer = 0
    width = len(maps[0]) - 1
    height = len(maps) - 1
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visit = [(0, 0)]
    queue = [(0, 0)]

    while queue:
        tmp = queue.pop(0)
        y = tmp[0]
        x = tmp[1]
        graph = [(y, x)]
        for my, mx in move:
            ny = y + my
            nx = x + mx
            if 0 <= ny <= height and 0 <= nx <= width and maps[ny][nx] == 1 and (ny, nx) not in visit:
                graph.append((ny, nx))
                queue.append((ny, nx))
        visit.append(graph)

    print(queue)
    print(visit)
    return answer

print(solution([[1,0,1,1,1],
                [1,0,1,0,1],
                [1,0,1,1,1],
                [1,1,1,0,1],
                [1,0,0,0,1]]))