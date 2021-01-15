# Programmers 01/13 2021
# 이상한 문자 만들기

def solution(s):
    answer = ''
    index = 0

    for x in s:
        if x == ' ':
            answer += x
            index = 0

        else:
            if index % 2 == 0:
                answer += x.upper()
                index = index + 1
            else:
                answer += x.lower()
                index = index + 1

    return answer

print(solution("try hello world"))