# Programmers 08/27 2021
# 월간 코드 첼린지 시즌2 - 약수의 개수와 덧셈

def divisorCnt(number):
    cnt = 1
    for n in range(1, (number//2)+1):
        if number % n == 0:
            cnt += 1
    return cnt


def solution(left, right):
    answer = 0

    for n in range(left, right+1):
        if divisorCnt(n) & 1:
            answer -= n
        else:
            answer += n

    return answer


print(solution(13, 17))
