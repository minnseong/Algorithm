# Programmers 07/18 2022
# 가장 긴 팰린드롬

def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if s[i:j] == s[i:j][::-1]:
                answer = max(answer, j-i)

    return answer

print(solution("abcdcba"))