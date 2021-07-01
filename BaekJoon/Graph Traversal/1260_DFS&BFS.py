from collections import deque


def dfs(graph_, start):
    visit = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            if node in graph_:
                stack.extend(sorted(graph_[node], reverse=True))

    return visit


def bfs(graph_, root):
    visit = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            if node in graph_:
                queue.extend(sorted(graph_[node]))

    return visit


inputInfo = list(map(int, input().split()))
edge = []
for _ in range(int(inputInfo[1])):
    tmp = list(map(int, input().split()))
    edge.append(tmp)

graph = {}

for g in edge:
    if g[0] not in graph:
        graph[g[0]] = [g[1]]
    else:
        graph[g[0]].append(g[1])

for g in edge:
    if g[1] not in graph:
        graph[g[1]] = [g[0]]
    else:
        graph[g[1]].append(g[0])

DFS = dfs(graph, inputInfo[2])
BFS = bfs(graph, inputInfo[2])

for i in DFS:
    print(i, end=' ')
print("")
for i in BFS:
    print(i, end=' ')