# Programmers 02/11 2021
# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0

    n = str(n)
    answer = "".join(sorted(n, reverse=True))

    return int(answer)

print(solution(118372))