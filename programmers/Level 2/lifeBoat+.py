# Programmers 03/02 2021
# 구명보트
# 효율성 테스트 1 성공 -> pop을 사용하지 않고 index로 접근

def solution(people, limit):
    answer = 0

    start = 0
    last = len(people) - 1

    people.sort()
    while start <= last:
        if people[start] + people[last] <= limit:
            start += 1
            last -= 1
        else:
            last -= 1

        answer += 1

    return answer

print(solution([70, 50, 80, 50]	, 100))
