# Programmers 03/26 2022
# 베스트 앨범

def solution(genres, plays):
    answer = []
    albumDic = dict()
    cntDic = dict()
    cntArray = []

    idx = 0
    for g, p in zip(genres, plays):
        if g not in albumDic:
            albumDic[g] = [[idx, p]]
        else:
            albumDic[g].append([idx, p])
        idx += 1
    
    for d in albumDic.values():
        d.sort(key=lambda x : (-x[1], x[0]))
    
    for k, v in albumDic.items():
        cntDic[k] = 0
        for vv in v:
            cntDic[k] += vv[1]
        cntArray.append([k, cntDic[k]])

    cntArray.sort(key=lambda x : -x[1])
    for ca in cntArray:
        for i in range(2):
            if len(albumDic[ca[0]]) == 1:
                answer.append(albumDic[ca[0]][i][0])
                break
            else:
                answer.append(albumDic[ca[0]][i][0])
            
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))