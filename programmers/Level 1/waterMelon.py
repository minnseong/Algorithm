# Programmers 02/08 2021
# 수박수박수박수박수박수박수박?

def solution(n):
    answer = ''

    if n & 1: # odd
        for i in range(int(n/2)):
            answer += "수박"
        answer += "수"

    else: # even
        for i in range(int(n/2)):
            answer += "수박"

    return answer

print(solution(6))