# Programmers 01/27 2021
# 자릿수 더하기

def solution(n):
    answer = 0

    while True:
        if n == 0:
            break

        answer += n % 10
        n = int(n / 10)

    return answer

print(solution(123))