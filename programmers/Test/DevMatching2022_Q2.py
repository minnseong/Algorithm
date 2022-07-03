# Programmers 07/03 2022
# 2022 Dev-Matching: 웹 백엔드 개발자(상반기)-2
# 100

def solution(n, horizontal):
    answer = [[0] * n for _ in range(n)]
    answer[0][0] = 1
    v = 2

    idx = [0, 0]
    for i in range(1, n):
        if horizontal:
            idx[1] += 1
            for _ in range(i+1):
                answer[idx[0]][idx[1]] = v
                v += 1
                idx[0] += 1
            idx[0] -= 1
            for _ in range(i):
                idx[1] -= 1
                answer[idx[0]][idx[1]] = v
                v += 1
            horizontal = False
        else:
            idx[0] += 1
            for _ in range(i+1):
                answer[idx[0]][idx[1]] = v
                v += 1
                idx[1] += 1
            idx[1] -= 1
            for _ in range(i):
                idx[0] -= 1
                answer[idx[0]][idx[1]] = v
                v += 1
            horizontal = True

    return answer

print(solution(5, False))