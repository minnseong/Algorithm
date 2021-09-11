# BaekJoon 09/11 2021
# 1978 소수 찾기

def isPrime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


N = int(input())
num = list(map(int, input().split()))
res = 0

for i in num:
    if i != 1 and isPrime(i):
        res += 1

print(res)
