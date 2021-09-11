# BaekJoon 09/11 2021
# 2581 소수

M = int(input())
N = int(input())
sum = 0
minValue = 0


def isPrime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


for i in range(M, N+1):
    if i != 1 and isPrime(i):
        if sum == 0:
            minValue = i
        sum += i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(minValue)
