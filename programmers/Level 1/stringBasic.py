# Programmers 02/08 2021
# 문자열 다루기 기본

def solution(s):

    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            return True
        else:
            return False
    else:
        return False

print(solution("a234"))