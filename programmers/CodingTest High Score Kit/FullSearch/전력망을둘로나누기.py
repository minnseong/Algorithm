from collections import defaultdict

def dfs(g, start, ex, n):
    cnt = 1
    stack = []
    visited = [False] * (n+1)
    for w in g[start]:
        if w != ex:
            stack.append(w)
    visited[start] = True
    while stack:
        s = stack.pop()
        visited[s] = True
        cnt += 1
        
        for w in g[s]:
            if not visited[w]:
                stack.append(w)

    return cnt

def solution(n, wires):
    graph = defaultdict(list)
    
    for w in wires:
        graph[w[0]].append(w[1])
        graph[w[1]].append(w[0])
        
    result = 1e9
    for w in wires:
        result = min(result, abs(dfs(graph, w[0], w[1], n)*2 - n))
    
    return result