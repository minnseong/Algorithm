# Programmers 11/27 2022
# 2022 카카오 모빌리티 코딩 테스트 Q1

def solution(flowers):
    answer = 0

    max_day = max([d[1] for d in flowers])

    days = [0] * (max_day+1)

    for day in flowers:
        start, end = day
        days[start] += 1
        days[end] -= 1

    for i in range(1, len(days)):
        days[i] += days[i-1]

    for d in days:
        if d >= 1:
            answer += 1

    return answer
