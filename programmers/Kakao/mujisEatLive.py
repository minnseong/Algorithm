# Programmers 05/06 2022
# 무지의 먹방 라이브

import heapq

def solution(food_times, k):
    answer = 0
    
    if sum(food_times) <= k:
        return -1

    heap = []
    i = 1
    for f in food_times:
        heapq.heappush(heap, (f, i))
        i += 1
    
    prv = 0
    while True:
        if (heap[0][0] - prv) * len(heap) <= k:
            k -= (heap[0][0] - prv) * len(heap)
            prv, _ = heapq.heappop(heap)
        else:
            heap.sort(key=lambda x: x[1])
            answer = heap[k%len(heap)][1]
            break
    
    return answer

print(solution([3, 1, 2], 5))