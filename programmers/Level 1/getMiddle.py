# Programmers 01/19 2021
# 가운데 글자 가져오기

def solution(s):
    answer = ''

    if len(s) & 1:
        answer = s[int(len(s)/2)]
    else:
        answer = s[int(len(s)/2) - 1] + s[int(len(s)/2)]
    return answer

print(solution("abcde"))