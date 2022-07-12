# Programmers 07/12 2022
# 가장 먼 노드

from collections import defaultdict, deque

def solution(n, edge):
    answer = 0

    distance = [0] * (n+1)
    edges = defaultdict(list)
    visited = [False] * (n+1)
    for e in edge:
        edges[e[0]].append(e[1])    
        edges[e[1]].append(e[0])    

    queue = deque([])
    queue.append([1, 0])
    
    while queue:
        x, d = queue.popleft()
        if visited[x]:
            continue 
        visited[x] = True
        distance[x] = d

        for e in edges[x]:
            if not visited[e]:
                queue.append([e, d+1])

    maxDistance = max(distance)
    for d in distance:
        if d == maxDistance:
            answer += 1
            
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))