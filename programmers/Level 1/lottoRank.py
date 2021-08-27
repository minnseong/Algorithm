# Programmers 08/27 2021
# 2021 Dev-Matching: 웹 백엔드 개발자(상반기) - 로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    answer = [7, 7]

    for l in lottos:
        if l == 0:
            answer[0] -= 1
        else:
            if l in win_nums:
                answer[0] -= 1
                answer[1] -= 1

    for i in range(len(answer)):
        if answer[i] == 7:
            answer[i] = 6

    return answer


print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
