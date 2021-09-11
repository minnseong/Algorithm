# BaekJoon 09/11 2021
# 2960 에라토스테네스의 체

def isPrime(num):
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True


N, K = map(int, input().split())

arr = [i for i in range(2, N+1)]

for i in range(len(arr)):
    if arr[i] != 0 and isPrime(arr[i]):
        P = arr[i]
        K -= 1
        if K == 0:
            print(arr[i])
        arr[i] = 0

        for j in range(i+1, len(arr)):
            if arr[j] != 0 and arr[j] % P == 0:
                K -= 1
                if K == 0:
                    print(arr[j])
                arr[j] = 0
