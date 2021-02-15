# Programmers 02/15 2021
# 프린터

def solution(priorities, location):
    answer = 0
    stk = []
    prior = priorities.copy()
    index = [i for i in range(len(priorities))]
    cnt = 0

    while prior:
        i = 0
        stk.append(prior[i])

        if prior[i] < max(prior):
            stk.pop()
            prior.append(prior[i])
            index.append(index[i])
            prior.pop(0)
            index.pop(0)

        else:
            cnt += 1
            if index[i] == location:
                answer = cnt
                break
            prior.pop(0)
            index.pop(0)

    return answer

print(solution([1,1,9,1,1,1], 0))
#print(solution([2,1,3,2],2))