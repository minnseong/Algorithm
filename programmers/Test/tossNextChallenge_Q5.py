# 08/06 2022 
# 2022 토스 NEXT 개발자 챌린지 - Q5

from collections import defaultdict

def solution(tasks):
    answer = 0

    dic = defaultdict(int)

    for t in tasks:
        dic[t] += 1
    
    for key in dic.keys():
        print(key)
        if dic[key] == 1:
            return -1
        if dic[key] == 2:
            answer += 1
            continue
        tmp = dic[key] % 3

        if tmp == 1:
            answer += (int(dic[key]/3) +1)
        elif tmp == 2:
            answer += (int(dic[key]/3) +1)
        elif tmp == 0:
            answer += (int(dic[key]/3))

    return answer