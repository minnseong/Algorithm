# Programmers 02/12 2021
# 콜라츠 추측

def solution(num):
    answer = 0

    while num != 1:
        if num & 1:
            num = num * 3 + 1
        else:
            num = int(num / 2)
        answer += 1

        if answer >= 500:
            answer = -1
            break

    return answer

print(solution(626331))