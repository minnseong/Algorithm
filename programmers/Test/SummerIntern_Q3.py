def chooseHand(right, left, target):
    r = abs(right[0]-target[0]) + abs(right[1]-target[1])
    l = abs(left[0]-target[0]) + abs(left[1]-target[1])

    if r > l:
        return "left"
    elif r < l:
        return "right"
    elif r == l:
        if abs(right[1]-target[1]) > abs(left[1]-target[1]):
            return "left"
        elif abs(right[1]-target[1]) < abs(left[1]-target[1]):
            return "right"
        else:
            return "check"

def solution(line):
    answer = []
    
    qwerty = "QWERTYUIOP"
    keys = [['1','2','3','4','5','6','7','8','9','0'], ['Q','W','E','R','T','Y','U','I','O','P']]
    dict = {}
    for i in range(len(keys)):
        for j in range(len(keys[0])):
            dict[keys[i][j]] = [i, j]
    
    left, right = [1,0], [1, 9]
    
    for l in line:
        pos = dict[str(l)]
        if chooseHand(right, left, pos) == "left":
            left = pos
            answer.append(0)
        elif chooseHand(right, left, pos) == "right":
            right = pos
            answer.append(1)
        else:
            if str(l) in set(['1', '2', '3', '4', '5', 'Q', 'W', 'E', 'R', 'T']):
                left = pos
                answer.append(0)
            else:
                right = pos
                answer.append(1)
    return answer

print(solution("Q4OYPI"))