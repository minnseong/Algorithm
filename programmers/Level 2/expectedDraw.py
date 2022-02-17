# Programmers 02/17 2022
# 예상 대진표

def getMaxRound(n):
    
    round = 0
    while (n != 1):
        n = n /2
        round += 1

    return round

def solution(n,a,b):
    
    answer = getMaxRound(n)
    standard = n / 2
    n = n / 4

    while True:
        if (a < standard + 0.5) and (b < standard + 0.5):
            standard = standard - n
            answer -= 1
            n /= 2
        elif (a > standard + 0.5) and (b > standard + 0.5):  
            standard = standard + n
            answer -= 1
            n /= 2
        else:
            break

    return answer

print(solution(8, 7, 8))