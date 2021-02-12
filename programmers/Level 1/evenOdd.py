# Programmers 02/11 2021
# 짝수와 홀수

def solution(num):
    answer = ''

    if num & 1:
        answer = "Odd"
    else:
        answer = "Even"

    return answer