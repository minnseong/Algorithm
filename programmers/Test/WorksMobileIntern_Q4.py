# Programmers 11/19 2022
# 2022 웍스모바일 인턴 코딩 테스트 Q4

from itertools import combinations_with_replacement

def getMultiple(arr):
    result = 1

    for a in arr:
        result *= a

    return result

def solution(n):
    answer = 0

    for i in range(2,n//2+1):
        for combi in list(combinations_with_replacement(range(2,n), i)):
            if sum(combi) == n:
                answer = max(answer, getMultiple(combi))

    return answer