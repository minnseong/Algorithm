# Programmers 01/21 2021
# 숫자의 표현

def solution(n):
    answer = 0
    s = 1

    while s != n:
        tmp = 0
        for i in range(s, n+1):
            tmp += i
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break
        s += 1

    return answer + 1

print(solution(15))