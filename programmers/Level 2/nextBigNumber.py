# Programmers 01/21 2021
# 다음 큰 숫자

def solution(n):
    answer = n
    n_binary = format(n, 'b')

    while True:
        answer += 1
        a_binary = format(answer, 'b')
        if n_binary.count("1") == a_binary.count("1"):
            break

    return answer

print(solution(78))