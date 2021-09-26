# BaekJoon 09/26 2021
# 1747 소수&팰린드롬

def isPrime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


N = int(input())

while True:
    if str(N) == str(N)[::-1]:
        if N != 1 and isPrime(N):
            print(N)
            break
    N += 1
