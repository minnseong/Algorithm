# SK텔레콤 코딩테스트 10/09 2022
# Q1

from collections import defaultdict

def solution(logs, events):
    answer = []

    users_history = defaultdict(list)

    for log in logs:
        t, user_name, event = log.split(" ")
        users_history[user_name].append(event)

    for k, v in users_history.items():
        cnt = 0
        for i in range(min(len(v), len(events))):
            if v[i] == events[i]:
                cnt += 1
            else:
                break
        if cnt != min(len(v), len(events)):
            answer.append(k)

    if answer:
        answer.sort()
    else:
        answer.append("-1")
    return answer