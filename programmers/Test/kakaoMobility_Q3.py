# Programmers 11/27 2022
# 2022 카카오 모빌리티 코딩 테스트 Q3

def calculate_time(year, month, day, hour, minute, second):

    if second > 59:
        minute += (second // 60)
        second %= 60
    if minute > 59:
        hour += (minute // 60)
        minute %= 60
    if hour > 23:
        day += (hour // 24)
        hour %= 24
    if day > 30:
        month += (day // 30)
        day %= 30
    if month > 12:
        year += (month // 12)
        month %= 12

    return [year, month, day, hour, minute, second]

def get_save_day(start, end):
    save_day = 0
    save_day += (end[2] - start[2] + 1)
    save_day += ((end[1] - start[1]) * 30)
    save_day += ((end[0] - start[0]) * 360)
    return save_day

def solution(s, times):
    answer = [1, 0]

    save_days = set()
    year, month, day, hour, minute, second = map(int, s.split(":"))
    save_days.add(str(year) + ":" + str(month) + ":" + str(day))

    for t in times:
        d, h, m, s = map(int, t.split(":"))

        year, month, day, hour, minute, second = calculate_time(year, month, day+d, hour+h, minute+m, second+s)
        save_days.add(str(year) + ":" + str(month) + ":" + str(day))

    save_days = sorted([list(map(int, save_day.split(":"))) for save_day in save_days], key=lambda x : (x[0], x[1], x[2]))

    answer[1] = get_save_day(save_days[0], save_days[-1])
    answer[0] = 1 if answer[1] == len(save_days) else 0
    return answer