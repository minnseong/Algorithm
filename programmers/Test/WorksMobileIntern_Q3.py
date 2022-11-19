# Programmers 11/19 2022
# 2022 웍스모바일 인턴 코딩 테스트 Q3

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def join(x, y):
    parent_x = find(x)
    parent_y = find(y)

    if parent_x > parent_y:
        parent[parent_x] = parent_y
    else:
        parent[parent_y] = parent_x

def solution(n, network, repair):
    answer = 0

    global parent
    parent = [i for i in range(n+1)]

    for net in network:
        join(net[0], net[1])

    repair.sort(key=lambda x : x[2])

    for r in repair:
        if find(r[0]) != find(r[1]):
            answer += r[2]
            join(r[0], r[1])    

    for i in range(1, len(parent)):
        if find(i) != 1:
            return -1

    return answer
