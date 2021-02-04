# Programmers 02/04 2021
# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    dic = {}

    for p in participant:
        if p not in dic:
            dic[p] = 1
        else:
            dic[p] += 1

    for p in completion:
        dic[p] -= 1

    for p in participant:
        if dic[p] is 1:
            answer = p

    return answer

print(solution(["a","b","c"],["b","c"]))