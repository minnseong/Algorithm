# Programmers 03/21 2021
# 괄호 변환


def isBalance(b):
    cnt = 0
    for i in range(len(b)):
        if b[i] == "(":
            cnt += 1
        else:
            cnt -= 1

    if cnt == 0:
        return True
    else:
        return False


def split(b):
    cnt = 0
    for i in range(len(b)):
        if b[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i+1

    return i+1


def solution(p):
    answer = ''

    return answer