# Programmers 04/08 2021
# KaKao 실패율

def solution(n, stages):
    answer = []

    last = [0 for i in range(n)]

    for i in range(1, n+1):  # 1~4
        if stages.count(i) == 0:
            last[i - 1] = 0
        else:
            last[i - 1] = stages.count(i) / len([x for x in stages if x >= i])

    sortedLast = sorted(last, reverse=True)

    for i in range(n):
        answer.append(last.index(sortedLast[i])+1)
        last[last.index(sortedLast[i])] = -1

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))