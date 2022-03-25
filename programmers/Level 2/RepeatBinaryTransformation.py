# Programmers 03/25 2022
# 이진 변환 반복하기

def removeZero(string):
    rs = ""
    zeroCnt = 0
    for s in string:
        if s == "0":
            zeroCnt += 1
        if s == "1":
            rs += "1"

    return rs, zeroCnt

def solution(s):
    answer = [0, 0]

    while s != "1":
        answer[0] += 1
        s, zeroCnt = removeZero(s)
        answer[1] += zeroCnt
        s = bin(len(s))[2:]

    return answer

print(solution("110010101001"))