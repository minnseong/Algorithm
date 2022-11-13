# Programmers 11/13 2022
# 2022 카카오뱅크 인턴 코딩 테스트 Q4
# 성공

from collections import defaultdict

def solution(jobs):
    answer = []

    importance_dict = defaultdict(int)
    duration_dict = defaultdict(int)

    time_table = [list() for _ in range((jobs[-1][0] + 1))]
    for job in jobs:
        time_table[job[0]].append(job[1:])

    t = jobs[0][0]
    until_t = t+1
    category = -1
    while t < jobs[-1][0] + 1:
        while t < jobs[-1][0]+1 and t < until_t:
            for job in time_table[t]:
                if job[1] == category:
                    until_t += job[0]
                else:
                    importance_dict[job[1]] += job[2]
                    duration_dict[job[1]] += job[0]
            t += 1

        category_list = sorted([key for key, value in importance_dict.items() if max(importance_dict.values()) == value])

        if len(category_list) >= 1:
            category = category_list[0]
            until_t = t + duration_dict[category]
            del importance_dict[category]
            del duration_dict[category]
            if len(answer) == 0 or len(answer) >= 1 and category != answer[-1]:
                answer.append(category)
        else:
            category = -1
            until_t += 1

    while True:
        category_list = sorted([key for key, value in importance_dict.items() if max(importance_dict.values()) == value])
        if len(category_list) >= 1:
            category = category_list[0]
            del importance_dict[category]
            del duration_dict[category]
            if len(answer) == 0 or len(answer) >= 1 and category != answer[-1]:
                answer.append(category)
        else:
            break

    return answer
