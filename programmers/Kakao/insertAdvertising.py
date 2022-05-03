# Programmers 05/03 2022
# 광고 삽입

def parsingTime(log):
    return log.split("-")   

def addTime(startTime, advTime):
    st = startTime.split(":")
    at = advTime.split(":")

    time = []
    for i in range(3):
        time.append(int(st[i])+ int(at[i]))
    for i in range(2, -1, -1):
        if i > 0 and time[i] >= 60:
            time[i] -= 60
            time[i-1] += 1
        if time[i] < 10:
            time[i] = '0' + str(time[i])
        else:
            time[i] = str(time[i])

    return ":".join(time)    

def minusTime(lastTime, advTime):
    lt = lastTime.split(":")
    at = advTime.split(":")

    time = []
    for i in range(3):
        time.append(int(lt[i]) - int(at[i]))
    
    for i in range(2, -1, -1):
        if time[i] < 0:
            time[i] += 60
            time[i-1] -= 1
        if time[i] < 10:
            time[i] = '0' + str(time[i])
        else:
            time[i] = str(time[i])

    return ":".join(time)   

def compareTime(time1, time2):
    cnt = 0
    for t1, t2 in zip(time1.split(":"), time2.split(":")):
        if int(t1) > int(t2):
            return True
        elif int(t1) == int(t2):
            cnt += 1
        else:
            return False
    if cnt == 3:
        return True
    return False 
    

def solution(play_time, adv_time, logs):
    answer = ''
    maxPlay = "00:00:00"

    if play_time == adv_time:
        return "00:00:00"

    for l in logs:
        startTime = l.split("-")[0]
        playTime = [startTime, addTime(startTime, adv_time)]
        tmpPlayTime = "00:00:00"
        for ll in logs:
            stll, ltll = ll.split("-")
            if compareTime(stll, playTime[0]) and compareTime(playTime[1], ltll):
                tmpPlayTime = addTime(tmpPlayTime, minusTime(ltll, stll))
            elif compareTime(stll, playTime[0]) and compareTime(playTime[1], stll):
                tmpPlayTime = addTime(tmpPlayTime, minusTime(playTime[1], stll))
            elif compareTime(ltll, playTime[0]) and compareTime(playTime[1], ltll):
                tmpPlayTime = addTime(tmpPlayTime, minusTime(ltll, playTime[0]))
        
        if compareTime(tmpPlayTime, maxPlay):
            maxPlay = tmpPlayTime
            answer = startTime

    return answer

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", "50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))