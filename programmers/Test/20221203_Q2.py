from collections import defaultdict
from itertools import combinations

def solution(n, edges, users, d, limit):
    answer = 0

    graph = [[1e9] * (n+1) for _ in range(n+1)]

    for e in edges:
        graph[e[0]][e[1]] = e[2]
        graph[e[1]][e[0]] = e[2]

    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    users_node = defaultdict(set)

    for i in range(len(users)):
        if users[i] != 0:
            for j in range(1, n+1):
                if graph[i+1][j] <= d:
                    users_node[i+1].add(j)
            users_node[i+1].add(i+1)


    for combi in list(combinations(range(1, n+1), 2)):
        tmp_answer = 0
        tmp_users = defaultdict(int)
        for c in combi:
            tmp_limit = limit
            for k, v in users_node.items():
                if c in v:
                    use_parking = min(tmp_limit, users[k-1]-tmp_users[k])
                    tmp_users[k] += use_parking
                    tmp_answer += use_parking
                    tmp_limit -= use_parking
                if tmp_limit <= 0:
                    break
        answer = max(answer, tmp_answer)

    return answer
