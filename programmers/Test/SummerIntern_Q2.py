# Programmers 05/08 2022
# 2022 Summer Coding - 여름 방학 스타트업 인턴 프로그램

from collections import defaultdict

def getNearDistacne(target, rooms):
    minDistance = int(1e9)
    for r in map(int, rooms):
        if minDistance >= abs(target-r):
            minDistance = abs(target-r)
    return minDistance

def priorityAlpha(name):
    if 'A' <= name[0] <= 'Z':
        return ord(name[0])-64
    else:
        return ord(name[0])

def solution(rooms, target):
    answer = []
    
    dict = defaultdict(list)
    excludeName = []
    for r in rooms:
        room, names = r.split(']')
        room = room[1:]
        for name in names.split(','):
            if room == str(target):
                excludeName.append(name)
            dict[name].append(room)
    
    for en in excludeName:
        del dict[en]
    for key in dict.keys():
        answer.append([key, len(dict[key]), getNearDistacne(target, dict[key])])
    answer.sort(key=lambda x: (x[1], x[2], x[0], priorityAlpha(x[0])))

    for i in range(len(answer)):
        answer[i] = answer[i][0]

    return answer

print(solution(["[403]James", "[404]Azad,Louis,louis", "[101]Azad,Guard"], 403))
# print(solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"], 202))