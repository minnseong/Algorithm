# Programmers 04/19 2022
# 빛의 경로 사이클

def solution(grid):
    answer = []

    dir = [[-1, 0], [1, 0], [0, -1], [0 , 1]] # 상, 하, 좌, 우

    visited = []
    for _ in range(len(grid)):
        tmp = []
        for _ in range(len(grid[0])):
            tmp.append([False] * 4) # 그 지점에서 나가는 방향 (상 하 좌 우) 
        visited.append(tmp)

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for d in range(4):
                if not visited[x][y][d]: # 나가는 방향 (상 하 좌 우)
                    visited[x][y][d] = True
                    travel(x, y, d, visited, grid)
                    

def travel(x, y, d, visited, grid):
    cnt = 0
    while True:
        dx = (x + dir[0][d]) % 4
        dy = (y + dir[1][d]) % 4
        cnt += 1

        if grid[dx][dy] == 'R':
            d = (d+3) % 4




    return answer

print(solution(["SL", "LR"]))