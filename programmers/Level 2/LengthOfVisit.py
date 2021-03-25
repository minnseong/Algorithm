# Programmers 03/25 2021
# 방문 길이

def solution(dirs):
    answer = 0
    dirArr = []
    point = [0, 0]

    for i in range(len(dirs)):
        if dirs[i] == "U":
            point.extend([point[0], point[1]+1])
            dirArr.append(point)
        if dirs[i] == "D":
            point.extend([point[0], point[1]-1])
            dirArr.append(point)
        if dirs[i] == "R":
            point.extend([point[0]+1, point[1]])
            dirArr.append(point)
        if dirs[i] == "L":
            point.extend([point[0]-1, point[1]])
            dirArr.append(point)

        point = point[2:]
        if point[0] > 5 or point[0] < -5 or point[1] > 5 or point[1] < -5:
            dirArr.pop(-1)
            point = dirArr[-1][2:]

    dirSet = []
    for d in dirArr:
        if d not in dirSet:
            dirSet.append(d)
    answer = len(dirSet)

    for d in dirSet:
        tmp = d[2:] + d[:2]
        if tmp in dirSet:
            answer -= 0.5

    return int(answer)

print(solution("ULURRDLLU"))
