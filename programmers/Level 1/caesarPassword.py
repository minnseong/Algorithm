# Programmers 02/10 2021
# 시저 암호

def solution(s, n):
    answer = ''
    ascii_list = []
    for k in range(len(s)):
        if ord(s[k]) == 32:  # spacebar
            ascii_list.append(32)
            continue

        tmp = ord(s[k]) + n
        if 65 <= ord(s[k]) <= 90 and 65 <= tmp <= 90:
            ascii_list.append(tmp)
        elif 97 <= ord(s[k]) <= 122 and 97 <= tmp <= 122:
            ascii_list.append(tmp)
        else:
            tmp = tmp - 26
            ascii_list.append(tmp)

    print(ascii_list)

    for a in ascii_list:
        answer += (chr(a))

    return answer

# print(solution("AB",1))
print(solution("Z", 25))
# print(solution("A", 25))