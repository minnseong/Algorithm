# Programmers 08/27
# 2018 KAKAO BLIND RECRUITMENT - 다트 게임

def solution(dartResult):
    answer = 0
    score = [0, 0, 0]

    idx = -1
    for d in dartResult:
        if d.isdigit():
            idx += 1
            if d == '0' and score[idx-1] == 1:
                score[idx-1] = 10
                idx -= 1
            else:
                score[idx] += int(d)
        else:
            if d == 'D':
                score[idx] *= score[idx]
            elif d == 'T':
                score[idx] *= (score[idx]*score[idx])
            elif d == '*':
                score[idx] *= 2
                if idx != 0:
                    score[idx-1] *= 2
            elif d == '#':
                score[idx] *= -1

    answer = sum(score)
    return answer


print(solution('1D2S#10S'))
