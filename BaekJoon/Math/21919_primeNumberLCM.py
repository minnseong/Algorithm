# BaekJoon 09/20 2021
# 21919 소수 최소 공배수

def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


N = int(input())
A = set(map(int, input().split()))

prime = 1

for a in A:
    if isPrime(a):
        prime *= a

if prime == 1:
    print(-1)
else:
    print(prime)
