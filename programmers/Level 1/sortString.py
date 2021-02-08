# Programmers 02/08 2021
# 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = []
    n_index = []

    for s in strings:
        n_index.append(s[n])

    n_index.sort()
    strings.sort()

    print(n_index)
    for c in n_index:
        for s in strings:
            if c == s[n]:
                answer.append(s)
                strings.remove(s)
                break

    return answer


print(solution(["sun", "bed", "car"], 1))
# print(solution(["abce", "abcd", "cdx"], 2))
