# Programmers 10/01 2022 다시 풀어보기 (코테 준비)
# KaKao 두 큐 합 같게 만들기

from collections import deque

def solution(queue1, queue2):
    answer = -2
    
    cnt = 0
    ptr = len(queue1)
    total_sum = sum(queue1) + sum(queue2)
    half_sum = 0
    
    if total_sum & 1:
        return -1
    else:
        half_sum = total_sum // 2

    queue = deque(queue1 + queue2)
    
    tmp_sum = sum(queue2)
    
    while tmp_sum != half_sum and cnt <= (3* len(queue1) -3):
        try:
            if tmp_sum > half_sum:
                tmp_sum -= queue[ptr]
                ptr += 1
            else:
                queue.append(queue.popleft())
                ptr -= 1
                tmp_sum += queue[-1]
            cnt += 1
        except:
            return -1
    
    if cnt == (3* len(queue1) -3) + 1:
        return -1
    
    return cnt