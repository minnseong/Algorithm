# BaekJoon 09/28 2021
# 22943 수

from itertools import permutations


def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


K, M = map(int, input().split())
permute = permutations([str(i) for i in range(10)], K)
prime = []
condi = []
cnt = 0

for i in range(2, 10**K):
    if isPrime(i):
        prime.append(i)
# print(len(prime))
for i in list(permute):
    num = ''.join(i)
    if num[0] == '0':
        continue
    else:
        for j in prime:
            if int(num) > j and int(num) != 2*j and isPrime(int(num) - j):
                # print(num)
                condi.append(int(num))
                break

for i in condi:
    while i % M == 0:
        i = i // M
    for j in prime:
        if i % j == 0 and isPrime(i//j):
            # print(i, end=" ")
            # print(j, end=" ")
            # print(i//j)
            # print("-------------------------------")
            cnt += 1
            break

print(cnt)
