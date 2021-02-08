# Programmers 02/08 2021
# 2016년

def solution(a, b):
    answer = ''
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    print((sum(days[0:a-1]) + b))
    answer = week[(sum(days[0:a-1]) + b) % 7]

    return answer

print(solution(5,24))

