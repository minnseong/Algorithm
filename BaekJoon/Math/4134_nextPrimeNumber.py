# BaekJoon 09/11 2021
# 4134 다음 소수

import sys
import math


def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())

    while True:
        if n != 0 and n != 1 and isPrime(n):
            print(n)
            break
        else:
            n += 1
