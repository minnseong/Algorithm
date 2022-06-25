# Programmers 06/25 2022
# 줄 서는 방법
# 참고 : https://roomedia.tistory.com/entry/프로그래머스-줄-서는-방법-연습문제-level3-파이썬-수학

import math

def solution(n, k):
    k -= 1
    answer = []
    numbers = list(range(1, n+1))
    
    for i in range(n, 0, -1):
        div, k = divmod(k, math.factorial(i-1))
        answer.append(numbers.pop(div))
        
    return answer

''' 시간 초과
from itertools import permutations

def solution(n, k):
    line = list(permutations([i for i in range(1, n+1)], n))
    return list(line[k-1])
'''