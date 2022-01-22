# Programmers 01/22 2022
# 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):

    answer = 0
    truckQueue = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    sumBridge = 0

    while bridge:
        answer += 1
        sumBridge -= bridge.popleft()

        if truckQueue:
            if truckQueue[0] + sumBridge <= weight:
                truck = truckQueue.popleft()
                bridge.append(truck)
                sumBridge += truck
            else:
                bridge.append(0)

    return answer

print(solution(100, 100 ,[10]))