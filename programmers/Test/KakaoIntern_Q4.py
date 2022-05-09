# Programmers 05/09 2022
# 2022 카카오 인턴 코딩 테스트 Q4
# 테스트 케이스 1~12, 15 성공, 나머지 시간 초과

from collections import defaultdict
import sys

def solution(n, paths, gates, summits):
    answer = []
    sys.setrecursionlimit(10000)

    gates = set(gates)
    summits = set(summits)
    graph = defaultdict(list)
    for p in paths:
        graph[p[0]].append([p[1], p[2]])
        graph[p[1]].append([p[0], p[2]])

    for k in graph.keys():
        graph[k].sort(key=lambda x:x[1])

    visited = [False] * (n + 1)
    stack = []
    global max_intensity
    max_intensity = 0

    def dfs(node, intensity, gate, summit):
        global max_intensity
        visited[node] = True
        stack.append([node, intensity])

        if node == summit:
            answer.append([summit, intensity])
            max_intensity = intensity
            stack.pop()
            return

        for g in graph[node]:
            if not visited[g[0]]:
                if not (g[0] != gate and g[0] in gates) and not (g[0] != summit and g[0] in summits):
                    if (max_intensity == 0) or max_intensity > g[1]:
                        if intensity >= g[1]:
                            dfs(g[0], intensity, gate, summit)
                            visited[g[0]] = False
                        else:
                            dfs(g[0], g[1], gate, summit)
                            visited[g[0]] = False
        stack.pop()

    for s in sorted(summits):
        for g in sorted(list(gates)):
            dfs(g, 0, g, s)
            visited = [False] * (n + 1)
            stack = []

    answer.sort(key=lambda x:(x[1], x[0]))
    return answer[0]

# print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))
# print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4]))
# print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3,7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 40], [2, 4, 60], [3, 5, 20], [4, 5, 6]], [1,2], [5]))
# print(solution(4, [[1, 2, 1], [2, 4, 3], [1, 3, 2], [3, 4, 4], [1,4,2], [2,3,5]], [1], [4]))
# print(solution(5, [[1, 5, 1], [2,5,100],[2,3,1],[2,4,1],[3,4,1],[5,3,1]], [4,2], [5]))