# Programmers 02/11 2021
# 정수 제곱근 판별

def solution(n):
    answer = 0

    for i in range(n+1):
        if i*i == n:
            answer = (i+1) * (i+1)
            break

    if answer == 0:
        answer = -1

    return answer

print(solution(1))