# Programmers 10/06 2022
# 주차 요금 계산

from collections import defaultdict
import math

def calculateTime(time):
    hour, minute = list(map(int, time.split(":")))
    
    return 60*hour + minute

def calculateFee(time, fees):
    if fees[0] >= time:
        return fees[1]
    else:
        return fees[1] + math.ceil((time-fees[0]) / fees[2]) * fees[3]
    

def solution(fees, records):
    answer = []
    car_dict = defaultdict(list)
    time_dict = defaultdict(int)
    
    for r in records:
        time, car_number, types = r.split(" ")
        car_dict[car_number].append(time)
    
    for k, v in car_dict.items():
        for i in range(0, len(v), 2):
            if i == len(v)-1:
                time_dict[k] += (calculateTime("23:59")-calculateTime(v[i]))
            else:
                time_dict[k] += (calculateTime(v[i+1])-calculateTime(v[i]))
            
    for k in sorted(time_dict.keys()):
        print(time_dict[k])
        answer.append(calculateFee(time_dict[k], fees))
        
    return answer
    
# Programmers 01/15 2022
# KaKao 주차 요금 계산
import math

def dateToMinutes(date):
    h, m = map(int, date.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees
    
    dic = dict()

    for r in records:
        time, number, history = r.split()
        number = int(number)
        
        if number in dic:
            dic[number].append([dateToMinutes(time), history])
        else:
            dic[number] = [[dateToMinutes(time), history]]
    
    rList = list(dic.items())
    rList.sort(key=lambda x : x[0])
    
    for r in rList:
        t = 0

        for rr in r[1]:
            if rr[1] == "IN":
                t -= rr[0]
            else:
                t += rr[0]

        if r[1][-1][1] == "IN":
            t += dateToMinutes('23:59')
        
        if t <= dt:
            answer.append(df)
        else:
            answer.append(df + math.ceil((t-dt) / ut) * uf)        

    return answer


print(solution([180, 5000, 10, 600],
["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	))

print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	))