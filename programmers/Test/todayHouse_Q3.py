# 07/16 2022 - Q3
# 오늘의 집 - Software Engineer, Intern, Corp Engineering

def getDistance(pos1, pos2):
    return abs(pos1[0]-pos2[0]) + abs(pos1[1]-pos2[1])

def solution(param0):
    answer = 0

    if (len(param0) == 2):
        return 0

    keyboard = dict()

    x, y = 0, 0
    for i in range(26):
        keyboard[chr(65+ i)] = [x, y]
        y += 1
        if y == 6:
            y = 0
            x += 1

    maxDistance = 0
    idx = 0
    for i in range(len(param0)-1):
        if getDistance(keyboard[param0[i]], keyboard[param0[i+1]]) > maxDistance:
            idx = i
            maxDistance = getDistance(keyboard[param0[i]], keyboard[param0[i+1]])
            if maxDistance == 9:
                break

    firstFinger, secondFinger = param0[0], param0[idx+1] 
    for i in range(1, len(param0)):
        if i <= idx:
            answer += getDistance(keyboard[firstFinger], keyboard[param0[i]])
            firstFinger = param0[i]
        elif i == idx+1:
            continue
        else:
            firstFingerDist = getDistance(keyboard[firstFinger], keyboard[param0[i]])
            secondFingerDist = getDistance(keyboard[secondFinger], keyboard[param0[i]])

            if firstFingerDist < secondFingerDist:
                answer += firstFingerDist
                firstFinger = param0[i]
            else:
                answer += secondFingerDist
                secondFinger = param0[i]


    return answer


# HAPPY
# H A -> 0 + 0 + 3 + 0 + 4
# H Y -> 0 + 2 + 5 + 0
# H P -> 0 + 2 + 0 + 0 + 4

# CAKE
# C A -> 0 + 0 + 3 + 1
# C K -> 0 + 2 + 0 + 1

# ABCDVWX
# A V -> 0 + 1 + 1 + 1 + 0 + 1 + 1 + 1
# A D -> 0 + 1 + 1 + 0 + 