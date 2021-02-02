# Programmers 02/02 2021
# 체육복

def solution(n, lost, reserve):

    cnt = 0

    for i in range(1, n+1):
        if i in lost and i in reserve:
            reserve.remove(i)
            lost.remove(i)

    for i in lost:
        if i+1 in reserve:
            reserve.remove(i+1)
            cnt += 1

        elif i-1 in reserve:
            reserve.remove(i-1)
            cnt += 1

    answer = n - len(lost) + cnt
    return answer


print(solution(5, [1,2,4,5], [2,3,4]))