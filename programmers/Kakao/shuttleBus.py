# Programmers 11/12 2022
# KaKao [1차] 셔틀버스

def solution(n, t, m, timetable):

    crew_time = [(int(t[:2]) * 60 + int(t[3:])) for t in timetable]
    crew_time.sort()

    bus_time = [9 * 60 + (t * i) for i in range(n)]

    i = 0
    for b in bus_time:
        cnt = 0
        while i < len(crew_time):
            if i < len(crew_time) and crew_time[i] <= b and cnt < m:
                i += 1
                cnt += 1
            else:
                break
        if cnt < m:
            answer = b
        else:
            answer = crew_time[i-1]-1

    return str(answer // 60).zfill(2) + ":" + str(answer % 60).zfill(2)