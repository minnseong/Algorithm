# Programmers 12/11 2021
# n^2 배열 자르기

def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        a = int(i/n)
        b = i%n
        if a < b:
            answer.append(b+1)
        else:
            answer.append(a+1)

    return answer

print(solution(3, 2, 5))