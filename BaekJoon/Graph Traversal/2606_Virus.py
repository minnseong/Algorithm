computer_num = int(input())
connect_num = int(input())
pair = []

for _ in range(connect_num):
    pair.append(input())

graph = {}

for p in pair:
    if p[0] not in graph:
        graph[p[0]] = [p[2]]
    else:
        graph[p[0]].append(p[2])

for p in pair:
    if p[2] not in graph:
        graph[p[2]] = [p[0]]
    else:
        graph[p[2]].append(p[0])

virus = graph['1']
checked = []

while True:
    initSize = len(virus)
    tmp = []

    for v in virus:
        if v in checked:
            continue
        checked.append(v)
        if v in graph:
            tmp.extend(graph[v])

    virus.extend(tmp)
    virus = list(set(virus))

    if initSize == len(virus):
        break

print(len(virus)-1)
