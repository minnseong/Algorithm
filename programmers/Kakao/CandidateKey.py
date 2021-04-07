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