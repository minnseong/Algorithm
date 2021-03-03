# Programmers 03/03 2021
# JadenCase 문자열 만들기

def solution(s):
    answer = ''
    s = s.lower()
    string = s.split(" ")

    for s in string:
        s = list(s)
        tmp = ""
        if s and s[0].isalpha() and s[0].islower():
            s[0] = chr(ord(s[0]) - 32)
        tmp = "".join(s)
        answer += tmp
        answer += " "

    answer = answer[:-1]

    return answer

print(solution("3people  asdf dffff"))