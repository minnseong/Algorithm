# 08/06 2022 
# 2022 토스 NEXT 개발자 챌린지 - Q2

def solution(levels):
    answer = 0

    if len(levels) <= 3:
        return -1

    p = int(len(levels) * (0.25))
    levels.sort()

    return levels[len(levels)-p]
