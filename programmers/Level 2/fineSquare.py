# Programmers 03/15 2021
# 멀쩡한 사각형
import math


def solution(w, h):
    answer = 0

    if w == h:
        return w * h - w
    if h == 1:
        return 0

    for i in range(1, w+1):
        answer += (h - math.ceil((h / w) * i))

    return answer * 2


print(solution(8,12))
