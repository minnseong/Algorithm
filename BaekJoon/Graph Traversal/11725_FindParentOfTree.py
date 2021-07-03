N = int(input())
tree = []
for _ in range(N-1):
    tree.append(list(map(int, input().split())))

makeTree = {}
for t in tree:
    if t[0] not in makeTree:
        makeTree[t[0]] = [t[1]]
    else:
        makeTree[t[0]].append(t[1])

for t in tree:
    if t[1] not in makeTree:
        makeTree[t[1]] = [t[0]]
    else:
        makeTree[t[1]].append(t[0])

parent = [0] * (N-1)

stack = [1]
visit = [False] * N

while stack:
    node = stack.pop()
    if not visit[node-1]:
        for i in makeTree[node]:
            if i >= 2 and parent[i-2] == 0:
                parent[i-2] = node
        visit[node-1] = True
        if node in makeTree:
            stack.extend(makeTree[node])

for i in parent:
    print(i)