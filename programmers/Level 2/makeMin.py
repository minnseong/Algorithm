# Programmers 01/29 2021
# 최솟값 만들기

def solution(A,B):
    answer = 0

    a = sorted(A)
    b = sorted(B, reverse = True)

    for i in range(0, len(A)):
        answer += a[i] * b[i]

    return answer

print(solution([1,4,2], [5,4,4]))
