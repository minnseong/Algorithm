# Programmers 02/08 2022
# 삼각 달팽이

def solution(n):
    answer = []
    snail = []
    cnt = 0

    for i in range(1, n+1):
        snail.append([0] * i)
        cnt += i
    
    dir = [[1, 0], [0, 1], [-1, -1]]
    x, y, idx = 0, 0 ,0

    snail[0][0] = 1
    value = 2
    while value <= cnt:
        x = x+dir[idx][0]
        y = y+dir[idx][1]

        if 0 <= x < n and 0 <= y < len(snail[x]):
            if snail[x][y] != 0:
                x = x-dir[idx][0]
                y = y-dir[idx][1]
                idx = (idx + 1) % 3
            else:
                snail[x][y] = value
                value += 1
        else:
            x = x-dir[idx][0]
            y = y-dir[idx][1]
            idx = (idx + 1) % 3

    for s in snail:
        answer.extend(s)

    return answer

print(solution(5))