# Programmers 03/22 2023
# 리코쳇 로봇

from collections import deque

def solution(board):
    answer = 0
    
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    weight = len(board[0])
    height = len(board)
    
    board = list(map(list, board))
    start = (0,0)
    end = (0,0)
    for i in range(height):
        for j in range(weight):
            if board[i][j] == 'R':
                start = (i, j, 0)
            if board[i][j] == 'G':
                end = (i, j)
                
    queue = deque([start])    
    visited = set()
    
    while queue:
        x, y, cost = queue.popleft()
        if (x, y) == end:
            answer = cost
            break
        
        for d in dir:
            dx = x+d[0]
            dy = y+d[1]
            while (0 <= dx < height and 0 <= dy < weight) and board[dx][dy] != 'D':
                dx += d[0]
                dy += d[1]
            
            dx -= d[0]
            dy -= d[1]
            if (dx, dy) not in visited:
                queue.append((dx,dy,cost+1))
                visited.add((dx, dy))
    
    if answer == 0:
        return -1
    
    return answer

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))