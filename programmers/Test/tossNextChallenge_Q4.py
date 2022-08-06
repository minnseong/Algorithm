# 08/06 2022 
# 2022 토스 NEXT 개발자 챌린지 - Q4

from collections import defaultdict

def solution(invitationPairs):
    answer = []

    dic = defaultdict(list)
    for i in invitationPairs:
        dic[i[0]].append(i[1])
    
    score = defaultdict(int)

    for key in dic.keys():
        score[key] += 10*len(dic[key])

        for key2 in dic[key]:
            if key2 in dic:
                score[key] += 3*len(dic[key2])
                for key3 in dic[key2]:
                    if key3 in dic:
                        score[key] += len(dic[key3])
    
    scores = sorted(score.items(), key = lambda x:-x[1])
    
    cnt = 3
    for s in scores:
        if cnt > 0:
            answer.append(s[0])
            cnt -= 1

    return answer