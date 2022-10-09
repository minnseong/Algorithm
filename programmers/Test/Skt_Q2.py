# SK텔레콤 코딩테스트 10/09 2022
# Q2

from itertools import product

def solution(receive, sell):
    answer = []

    n = len(receive)
    diff = []

    for i in range(n):
        tmp = []
        for j in range(len(receive[i])):
            tmp.append(receive[i][j] - sell[i][j])
        diff.append(tmp)

    for p in list(product(range(n), repeat=5)):
        items = [0] * n
        cnt = 0
        for idx, pp in enumerate(p):
            for i in range(n):
                items[i] += diff[i][idx]
                if items[i] <= 0:
                    items[i] = 0

            cnt += items[pp]
            items[pp] = 0

        answer.append([cnt, p])
    answer.sort(key=lambda x: -x[0])
    print(answer)
    return answer[0][-1]

print(solution([[10,10,10,10,10], [5,5,13,5,10]], [[7,10,5,10,5], [0,5,0,35,5]]))

# 답 (0, 0, 1, 0, 0) -> 31개 가질 수 있음.