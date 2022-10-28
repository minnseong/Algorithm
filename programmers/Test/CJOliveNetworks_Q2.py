# Programmers 10/28 2022
# 2022 CJ 올리브네트웍스 Q2

from collections import defaultdict

def solution(n, edges):
    answer = []

    graph = defaultdict(set)

    for e in edges:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])


    for i in range(len(edges)):
        graph[edges[i][0]].remove(edges[i][1])
        graph[edges[i][1]].remove(edges[i][0])
        for e in edges[i]:
            stack = [e]
            visited = [False] * n
            cnt = 0
            while stack:
                s = stack.pop()
                cnt += 1

                visited[s] = True
                for node in graph[s]:
                    if not visited[node]:
                        stack.append(node)
            if cnt == n // 3:
                answer.append(i)

        graph[edges[i][0]].add(edges[i][1])
        graph[edges[i][1]].add(edges[i][0])

    return sorted(answer)
