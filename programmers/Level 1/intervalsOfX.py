# Programmers 02/12 2021
# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    tmpX = x

    for i in range(n):
        answer.append(x)
        x += tmpX

    return answer

print(solution(2, 5))