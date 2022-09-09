# Programmers 09/09 2022 다시 풀어보기 (코테 준비)
# Kakao 순위 검색

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left, bisect_right

def solution(info, query):
    querys = [q.replace("- ", "").replace("and ", "").split(" ") for q in query]
    user_infos = [i.split(" ") for i in info]
    
    dic = defaultdict(list)
    for u in user_infos:
        score = int(u[-1])
        for i in range(0, 5):
            combi = list(combinations(u[:-1], i))
            for c in combi:
                dic[''.join(c)].append(score)
                
    for key in dic.keys():
        dic[key].sort()
                
    result = []
    for qs in querys:
        score = int(qs[-1])
        c = "".join(qs[:-1])
        result.append(len(dic[c])-bisect_left(dic[c], score))
    
    return result

# Programmers 02/10 2021
# Kakao 순위 검색
# 정확성 테스트 100%, 효율성 테스트 0%
from itertools import combinations


def solution(info, query):

    answer = []
    db = {}
    for i in info:
        i = i.split()
        condition = i[:-1]
        score = int(i[-1])
        for n in range(5):
            combi = list(combinations([0, 1, 2, 3], n))
            for c in combi:
                tmpConditon = condition.copy()
                for d in c:
                    tmpConditon[d] = '-'
                tmpJoin = '/'.join(tmpConditon)
                if tmpJoin in db:
                    db[tmpJoin].append(score)
                else:
                    db[tmpJoin] = [score]

    for key in db.keys():
        db[key].sort()

    for q in query:
        q = q.split(' ')
        for i in range(3):
            q.remove('and')
        qCondition = '/'.join(q[:-1])
        qScore = int(q[-1])

        if qCondition in db:
            cnt = db[qCondition]
            if len(cnt) > 0:
                start, end = 0, len(cnt)
                while start != end and start != len(cnt):
                    if cnt[(start + end) // 2] >= qScore:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(cnt) - start)
        else:
            answer.append(0)

    return answer


Q_info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50"
]
Q_query = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150"
]

print(solution(Q_info, Q_query))
