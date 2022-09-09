# Programmers 09/09 2022 다시 풀어보기 (코테 준비)
# Kakao 후보키

from itertools import combinations

def combine_keys(keys, index):
    combine_keys_list = []
    
    for i in range(len(keys[0])):
        combine_key = ""
        for j in range(len(index)):
            combine_key += keys[index[j]][i]
        combine_keys_list.append(combine_key)
    return combine_keys_list
    
def solution(relation):
    
    res = 0
    keys = []
    for i in range(len(relation[0])):
        tmp = []
        for j in range(len(relation)):
            tmp.append(relation[j][i])
        keys.append(tmp)
    
    # print(keys)
    not_unique_keys = []
    for i in range(len(keys)):
        if len(set(keys[i])) == len(keys[i]):
            res += 1
        else:
            not_unique_keys.append(i)
    
    candidate_keys = [] # 1 2 3
    for i in range(2, len(not_unique_keys)+1):
        candidate_keys.extend(combinations(not_unique_keys, i))
    
    candidate_keys.sort(key=len)
    exclude_keys = []
    for c in candidate_keys:
        flag = False
        for ex in exclude_keys:
            if ex & set(c) == ex:
                flag = True
                break

        if not flag and len(set(combine_keys(keys, c))) == len(combine_keys(keys, c)):
            res += 1
            exclude_keys.append(set(c))
    
    
    print(set([(1,2,3), (1,2,3)]))
    return res
        
# Programmers 04/04 2021
# KaKao 후보키
from itertools import combinations


def solution(relation):
    answer = 0
    # 열의 갯수로 접근!
    col = len(relation[0])  # 4
    row = len(relation)
    unique = []  # 유일성을 만족한 속성을 담을 list
    colList = [i for i in range(col)]

    # 유일성을 만족하는 하나 속성 거르기.
    for i in range(col):
        tmp = []
        for j in range(row):
            tmp.append(relation[j][i])
        if len(tmp) == len(set(tmp)):
            setTemp = set()
            setTemp.add(i)
            unique.append(setTemp)
            answer += 1

    for i in range(2, col+1):  # 2~4
        combi = []
        combi += (list(combinations(colList, i)))
        print(combi)
        for j in range(len(combi)):
            for u in unique:
                if set(combi[j]) & u == u:
                    combi[j] = tuple()

        for w in combi:
            if w:
                temp = set()
                for r in range(row):  # 0~6
                    tmp = []
                    for s in w:
                        tmp.append(relation[r][s])
                    temp.add(tuple(tmp))

                if len(temp) == row:
                    w = set(w)
                    unique.append(w)
                    answer += 1

    return answer

print(solution([["100","ryan","music","2"],
                ["200","apeach","math","2"],
                ["300","tube","computer","3"],
                ["400","con","computer","1"],
                ["500","muzi","music","3"],
                ["600","apeach","music","2"]]))

#{0}, {(1,2)}
#{1,2,3}

print({1,2} & {1,2,3} == {1,2})