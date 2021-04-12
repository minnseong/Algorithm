# Programmers 04/10 2021
# KaKao 방금그곡

def solution(m, musicinfos):
    length = 0
    answer = '(None)'

    for w in musicinfos:
        start, end, name, sheet = w.split(',')
        code = []

        for c in sheet:
            if c != '#':
                code.append(c)
            else:
                code[-1] += c

        start = int(start[:2]) * 60 + int(start[-2:])
        end = int(end[:2]) * 60 + int(end[-2:])
        time = end - start

        full_code = ''

        while time:
            if time < 1:
                break
            full_code += ''.join(code[:time])
            time -= len(code)
        match_count = full_code.count(m)

        if match_count > 0 and match_count != full_code.count(m + '#'):
            if length < end - start:
                length = end - start
                answer = name

    return answer


print(solution("ABCDEFG", ["09:40,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
