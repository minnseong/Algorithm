# Programmers 08/27 2021
# 월간 코드 첼린지 시즌2 - 음양 더하기

def solution(absolutes, signs):
    answer = 0

    for i, j in zip(absolutes, signs):
        if j:
            answer += i
        else:
            answer -= i

    return answer


print(solution([4, 7, 12], [True, False, True]))
