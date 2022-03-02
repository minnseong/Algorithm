# Programmers 03/02 2022
# 네트워크

from collections import deque

def solution(n, computers):
    answer = 0

    dic = dict()
    for idx, val in enumerate(computers):
        dic[idx+1] = [idx+1]
        for i, v in enumerate(val):
            if i != idx and v == 1:
                dic[idx+1].append(i+1)
    
    queue = deque([])
    visited = [False for _ in range(n+1)] 
    visited[0] = True

    for i in range(1, n+1):
        if visited[i] == False:
            visited[i] = True
            queue.extend(dic[i])
            while queue:
                cp = queue.popleft()
                if visited[cp] == False:
                    visited[cp] = True
                    queue.extend(dic[cp])
            answer += 1               

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))