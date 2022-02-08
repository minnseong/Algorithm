# Programmers 02/09 2022
# 교점에 별 만들기

def getVertex(l1, l2):
    if l1[0]*l2[1] - l1[1]*l2[0] != 0:
        y = (l1[2]*l2[0] - l1[0]*l2[2]) / (l1[0]*l2[1] - l1[1]*l2[0])
        x = (l1[1]*l2[2] - l1[2]*l2[1]) / (l1[0]*l2[1] - l1[1]*l2[0])
        return y, x
    else:
        return 1.1, 1.1

def solution(line):
    answer = []
    vertex = []

    for i in range(len(line)):
        for j in range(i+1, len(line)):
            y, x  = getVertex(line[i], line[j])

            if int(x) == x and int(y) == y:
                vertex.append([int(y), int(x)])
    
    xMin, xMax = min(vertex, key=lambda x:x[1])[1], max(vertex, key=lambda x:x[1])[1]
    yMin, yMax = min(vertex, key=lambda x:x[0])[0], max(vertex, key=lambda x:x[0])[0]

    for y in range(yMin, yMax+1):
        tmp = ""
        for x in range(xMin, xMax+1):
            if [y, x] in vertex:
                tmp += "*"
            else:
                tmp += "."

        answer.append(tmp)

    answer.reverse()
                
    return answer

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))