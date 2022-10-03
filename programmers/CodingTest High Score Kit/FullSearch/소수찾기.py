from itertools import permutations
import math

def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(numbers):
    
    ans = 0
    
    permu = []
    for i in range(1, len(numbers)+1):
        permu.extend(permutations(list(numbers), i))
    
    for p in set(permu):
        if ''.join(p)[0] == '0':
            print(''.join(p))
            continue
        else:
            if isPrime(int(''.join(p))):
                ans += 1
    
    return ans