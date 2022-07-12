# Programmers 07/12 2022
# 야근 지수

import heapq

def solution(n, works):
    answer = 0

    if n > sum(works):
        return 0

    heap = []
    for w in works:
        heapq.heappush(heap, -w)

    for _ in range(n):
        h = heapq.heappop(heap)
        h += 1
        heapq.heappush(heap, h)
    
    for h in heap:
        answer += (h*h)

    return answer

print(solution(4, [4,3,3]))
print(solution(9, [1,1,1]))