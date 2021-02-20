# Programmers 02/20 2021
# KaKao 신규 아이디 추천

# 알파벳 소문자, 숫자, -, _, .
def solution(new_id):
    answer = ''

    tmp = list(new_id.lower())

    for s in tmp:
        if s == "." or s == "-" or s == "_" or s.isalpha() or s.isdigit():
            answer += s

    while ".." in answer:
        answer = answer.replace("..", ".")

    if len(answer) != 0:
        if answer[0] == ".":
            answer = answer[1:]

    if len(answer) != 0:
        if answer[-1] == ".":
            answer = answer[:-1]

    if not answer:
        answer = "a"

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))