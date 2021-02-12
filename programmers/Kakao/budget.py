# Programmers 02/12 2021
# KaKao 예산

def solution(d, budget):
    answer = 0
    bud = 0

    d.sort()
    for i in d:
        bud += i
        if bud > budget:
            break
        answer += 1

    return answer

print(solution([1,3,2,5,4], 9))
