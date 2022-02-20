# Programmers 02/20 2022
# 배달

import math

def getSmallDistance(d, v):
    min = math.inf

    for idx, val in enumerate(d):
        if min > val and not v[idx]:
            min = val
            i = idx
    return i

def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N+1)]
    distance = [math.inf] * (N + 1)
    visited = [False] * (N + 1)
    
    for r in road:
        graph[r[0]].append([r[1], r[2]])
        graph[r[1]].append([r[0], r[2]])
    
    for g in graph[1]:
        if distance[g[0]] > g[1]:
            distance[g[0]] = g[1]

    distance[0] = 0
    distance[1] = 0
    visited[0] = True
    visited[1] = True
    
    for _ in range(N-1):
        idx = getSmallDistance(distance, visited)
        visited[idx] = True
        for g in graph[idx]:
            if distance[g[0]] > distance[idx] + g[1]:
                distance[g[0]] = distance[idx] + g[1]

    for i in range(1, N+1):
        if distance[i] <= K:
            answer += 1

    return answer

print(solution(2, [[2,1,5],[1,2,6]], 5))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))