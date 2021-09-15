# Programmers 09/15 2021
# 위클리 챌린지 - 5주차 모음사전

# A E I O U
def solution(word):
    answer = 0
    wordToNum = {'A': '1', 'E': '2', 'I': '3', 'O': '4', 'U': '5'}
    tmp = '0.'

    for w in word:
        tmp += wordToNum[w]

    print(tmp)

    return answer


print(solution("AAAE"))
