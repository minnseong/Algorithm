# Programmers 05/09 2022
# 2022 카카오 인턴 코딩 테스트 Q2
# 성공

from collections import deque

def solution(queue1, queue2):
    answer = 0

    total_len = len(queue1) + len(queue2)
    queue1_sum = sum(queue1)
    queue2_sum = sum(queue2)
    total = queue1_sum + queue2_sum

    if total & 1:
        return -1

    queue1 = deque(queue1)
    queue2 = deque(queue2)

    while True:
        if queue1_sum == total//2 and queue2_sum == total//2:
            break
        if answer > total_len*2:
            answer = -1
            break

        if queue1_sum > total//2:
            queue1_sum -= queue1[0]
            queue2_sum += queue1[0]
            queue2.append(queue1.popleft())
            answer += 1
        elif queue1_sum < total//2:
            queue1_sum += queue2[0]
            queue2_sum -= queue2[0]
            queue1.append(queue2.popleft())
            answer += 1

    return answer

print(solution([2,5,1], [5,2,2]))