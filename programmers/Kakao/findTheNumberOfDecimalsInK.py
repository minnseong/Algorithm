# Programmers 01/27 2022
# KaKao k진수에서 소수 개수 구하기

'''
    시간초과로 다른 사람의 코드 확인

    이전 코드에서는 소수판별시, 어떤 수 n을 2부터 n//2+1 까지 나눈 나머지가 모두 0이 아님을 확인한 방법을 썼으나
    -> 시간초과
    -> 소수판별시, 어떤 수 n을 2부터 루트(n)까지 나눈 나머지가 모두 0이 아님을 확인하는 방법을 써야함

    문제에서는 10진법을 3~10진법으로 변환하는 거라 어렵지 않았으나, 
    10진수를 2-16진수까지 변환하는 경우 코드 첨부

    def convert_notation(n, k):
        notation = ''
        T = "0123456789ABCDEF"
        while n > 0:
            n, mod = divmod(n, k)
            notation += T[mod]

        return notation[::-1]
'''

import math

def isPrime(num):

    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True
    

def solution(n, k):
    answer = 0

    # 진법 변환 - 3~10 진법까지
    notation = ''

    while n > 0:
        n, mod = divmod(n, k)
        notation += str(mod)
    
    notation = notation[::-1]
    
    for i in notation.split('0'):
        if i:
            if isPrime(int(i)):
                answer += 1

    return answer

print(solution(437674, 3))