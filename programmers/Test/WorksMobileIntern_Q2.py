# Programmers 11/19 2022
# 2022 웍스모바일 인턴 코딩 테스트 Q2

def solution(A,S):
    answer = 1e9

    i = 0
    j = 0
    tmp_sum = 0
    while i <= j < len(A):
        if tmp_sum >= S:
            answer = min(answer, j-i)
            tmp_sum -= A[i]
            i += 1
        else:
            tmp_sum += A[j]
            j += 1

    while tmp_sum >= S and i < len(A):
        tmp_sum -= A[i]
        i += 1
        answer = min(answer, j-i+1)

    if answer == 1e9:
        answer = 0

    return answer