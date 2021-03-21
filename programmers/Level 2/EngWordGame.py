# Programmers 03/21 2021
# 영어 끝말잇기

def solution(n, words):
    answer = []

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            break

        if words[i] in words[0:i]:
            answer.append((i % n) + 1)
            answer.append((i // n) + 1)
            break

    if not answer:
        answer = [0, 0]

    return answer