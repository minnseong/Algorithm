computer_num = int(input())
connect_num = int(input())
pair = []

for _ in range(connect_num):
    pair.append(input().split())
graph = {}

for p in pair:
    if p[0] not in graph:
        graph[p[0]] = [p[1]]
    else:
        graph[p[0]].append(p[1])

for p in pair:
    if p[1] not in graph:
        graph[p[1]] = [p[0]]
    else:
        graph[p[1]].append(p[0])

if '1' in graph:
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
        tmp = list(set(tmp))
        virus.extend(tmp)
        virus = list(set(virus))

        if initSize == len(virus):
            break

    if '1' in virus:
        print(len(virus) - 1)
    else:
        print(len(virus))
else:
    print(0)


