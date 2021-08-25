# Programmers 08/26 2021
# Kakao 숫자 문자열과 영단어

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']

    for idx in range(len(words)):
        s = s.replace(words[idx], str(idx))

    return int(s)


print(solution("one4seveneight"))
