# Programmers 05/03 2022
# 광고 삽입

def timeToSecond(time):
    time = time.split(":")
    hour = int(time[0]) * 3600
    minute = int(time[1]) * 60
    second = int(time[2])
    return hour + minute + second

def secondToTime(second):
    hour = second // 3600
    hour = '0' + str(hour) if hour < 10 else str(hour)
    minute = (second % 3600) // 60
    minute = '0' + str(minute) if minute < 10 else str(minute)
    second = second % 60
    second = '0' + str(second) if second < 10 else str(second)
    return str(hour) + ":" + str(minute) + ":" + str(second)

def solution(play_time, adv_time, logs):
    answer = ''

    time = [0] * (timeToSecond(play_time) + 1)

    for l in logs:
        s, e = l.split("-")
        time[timeToSecond(s)] += 1
        time[timeToSecond(e)] -= 1
    
    for i in range(1, timeToSecond(play_time)):
        time[i] = time[i] + time[i-1]
    for i in range(1, timeToSecond(play_time)):
        time[i] = time[i] + time[i-1]
    
    maxTime = 0
    for i in range(timeToSecond(adv_time)-1, timeToSecond(play_time)):
        tmp = time[i] - time[i-timeToSecond(adv_time)]
        if maxTime < tmp:
            maxTime = tmp
            answer = i - timeToSecond(adv_time) + 1

    return secondToTime(answer)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
# print(solution("50:00:00", "50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))