# Programmers 01/19 2021
# 소수 찾기

# set 사용
def solution(n):
    answer = 0
    num_set = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num_set:
            num_set -= set(range(2*i, n+1, i))

    answer = len(num_set)
    return answer

print(solution(10))

'''
test 10, 11, 12 시간초과
def solution(n):
    answer = 0
    cnt = 0

    for i in range(1, n+1):
        for j in range(2, i):
            if i % j == 0:
                cnt = 1
                break
        if i > 1 and cnt == 0:
            answer += 1
        cnt = 0

    return answer
'''