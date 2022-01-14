# Programmers 01/14 2022
# KaKao 신고 결과 받기

def disposeReport(reportList, k):

    dic = dict()
    stopSet = set()

    for r in reportList:
        rter, rted = r.split()

        if rted in dic:
            dic[rted].append(rter)
        else:
            dic[rted] = [rter]
        
    for d in dic.keys():
        if len(dic[d]) >= k:
            stopSet.add(d)
    
    return dic, stopSet

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    indexID = dict()
    idx = 0

    for id in id_list:
        indexID[id] = idx
        idx += 1

    reportDic, stopSet = disposeReport(list(set(report)), k)
    
    for d in reportDic:
        if d in stopSet:
            for v in reportDic[d]:
                answer[indexID[v]] += 1
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))