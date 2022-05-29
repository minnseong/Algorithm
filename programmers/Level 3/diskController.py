# Programmers 05/29 2022
# 디스크 컨트롤러

import heapq

def solution(jobs):
    answer = 0
    cnt = len(jobs)
    for i in range(len(jobs)):
        jobs[i].reverse()
    
    jobs.sort(key=lambda x:-x[1])
    heap = []
    time = jobs[-1][1]
    idx = 0
    while idx < cnt:
        for i in range(len(jobs)):
            if jobs[-1][1] <= time:
                heapq.heappush(heap, jobs.pop())

        if heap:
            j = heapq.heappop(heap)
            answer += (time+j[0]-j[1])
            time += j[0]
            idx += 1
        else:
            time += 1

    return answer // cnt

# print(solution([[0, 3], [1, 9], [2, 6]]	))
print(solution([[0, 3], [5, 9], [6, 6]])) # 3+6+16
