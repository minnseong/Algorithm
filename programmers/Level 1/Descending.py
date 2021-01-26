# Progammers 01/26 2021
# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''

    s_list = list(s)
    s_list.sort(reverse=True)

    answer = ''.join(s_list)
    return answer

print(solution("Zbcdefg"))