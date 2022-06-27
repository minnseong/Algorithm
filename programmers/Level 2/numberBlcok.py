# Programmers 06/27 2022
# 숫자 블록

import math

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0 and num // i <= 10000000:
            return num // i
    return -1


def solution(begin, end):
    answer = []

    if begin == 1:
        answer.append(0)
        begin += 1

    for i in range(begin, end+1):
        if isPrime(i) == -1:
            answer.append(1)
        else:
            answer.append(isPrime(i))

    return answer


print(solution(100000, 100500))

''' 시간초과
import math

def solution(begin, end):
    answer = [1] * (end-begin+1)
    visited = [False] * (end-begin+1)

    start = end // 2

    for idx in range(start, int(math.sqrt(begin)), -1):
        i = 2
        while idx * i <= end:
            if 0 <= (idx*i - begin) <= (end-begin) and not visited[(idx*i - begin)]:
                answer[(idx*i - begin)] = idx
                visited[(idx*i - begin)] = True
            i+= 1

    if begin == 1:
        answer[0] = 0

    return answer
'''