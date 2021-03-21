# Programmers 03/21 2021
# 소수 찾기
from itertools import permutations
import math


def solution(numbers):
    prime = []

    for i in range(1, len(numbers)+1):
        perm = set(permutations(numbers, i))
        for j in perm:
            j = int("".join(map(str, j)))
            flag = True
            for n in range(2, int(math.sqrt(int(j)))+1):
                if int(j) % n == 0:
                    flag = False
            if flag is True:
                prime.append(j)

    prime = set(prime)
    print(prime)
    answer = len(prime)
    if 0 in prime:
        answer -= 1
    if 1 in prime:
        answer -= 1

    return answer

print(solution("011"))