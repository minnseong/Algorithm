# Programmers 11/13 2022
# 2022 카카오뱅크 인턴 코딩 테스트 Q1
# 성공

def solution(logs):
    answer = [0] * 24

    for log in logs.split("\n"):
        day, time = log.split(" ")
        hour = (int(time[:2]) + 9) % 24
        answer[hour] += 1

    return answer
