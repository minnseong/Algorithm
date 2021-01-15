# Programmers 01/13 2021
# 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = []

    while n > 0:
        answer.append(n % 10)
        n = int(n / 10)

    return answer

print(solution(12345))