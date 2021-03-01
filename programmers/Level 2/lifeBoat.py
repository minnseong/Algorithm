# Programmers 03/02 2021
# 구명보트
# 효율성 테스트 1 실패

def solution(people, limit):
    answer = 0

    people.sort()
    while people:
        if len(people) >= 2 and people[0] + people[-1] <= limit:
            people.pop(0)
            people.pop()
        else:
            people.pop()

        answer += 1

    return answer

print(solution([70, 50, 80, 50]	, 100))