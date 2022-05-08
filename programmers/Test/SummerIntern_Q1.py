# Programmers 05/08 2022
# 2022 Summer Coding - 여름 방학 스타트업 인턴 프로그램

def solution(atmos):
    answer = 0
    reuse = 0

    for a in atmos:
        if a[0] >= 151 and a[1] >= 76: # 둘다 매우 나쁨
            if reuse != 0:
                reuse = 0
            else:
                answer += 1
                reuse = 0
        elif a[0] >= 81 or a[1] >= 36:
            if reuse == 0:
                reuse = 3
            if reuse == 3:
                answer += 1
                reuse -= 1
            elif reuse != 0:
                reuse -= 1
        else:
            if reuse != 3 and reuse != 0:
                reuse -= 1

    return answer

print(solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]]))
print(solution([[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]]))
print(solution([[300, 150], [800, 305]]))