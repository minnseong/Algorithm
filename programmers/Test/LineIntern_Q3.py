# Programmers 05/28 2022
# 2022 라인 인턴 코딩 테스트 Q3

from itertools import product
import math

def divFuel(fuel, num):
    return [list(x) for x in product(range(1, fuel), repeat=num) if sum(x) == fuel]

def getReachTime(fuel, power, distance):
    time = fuel
    speed = fuel * power
    distance -= ((speed*fuel)/2)
    time += (distance / speed)
    return time

def solution(fuel, powers, distances):

    allCase = divFuel(fuel, len(powers))

    maxTime = []
    for a in allCase:
        mxTime = 0
        for i in range(len(a)):
            if getReachTime(a[i], powers[i], distances[i]) > mxTime:
                mxTime = getReachTime(a[i], powers[i], distances[i])
        maxTime.append(mxTime)

    return math.ceil(min(maxTime))

print(solution(8, [20, 30], [750, 675]))
print(solution(19, [40, 30, 20, 10], [1000, 2000, 3000, 4000]))