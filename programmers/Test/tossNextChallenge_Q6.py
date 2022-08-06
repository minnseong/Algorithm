# 08/06 2022 
# 2022 토스 NEXT 개발자 챌린지 - Q6

from collections import defaultdict

def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = []

    dic = defaultdict(list)
    check = set()

    for ss, nn in zip([steps_one, steps_two, steps_three], [names_one, names_two, names_three]):
        check = set()
        for s, n in zip(ss, nn):
            if n in check:
                dic[n][-1] = max(dic[n][-1], s)
            else:
                dic[n].append(s)
                check.add(n)
    
    for key in dic.keys():
        dic[key] = sum(dic[key])
    
    sd = sorted(dic.items(), key = lambda item: (-item[1], item[0]))
    for s in sd:
        answer.append(s[0])
    
    return answer