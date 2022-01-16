# Programmers 01/17 2022
# KaKao 튜플

def solution(s):
    answer = []

    s = s[2:-2]
    arr = s.split("},{")
    tupleSet = []
    tupleList = []

    for a in arr:
        tupleSet.append(set(map(int, a.split(','))))
        tupleList.append(list(map(int, a.split(','))))

    tupleSet.sort(key=lambda x: len(x))
    tupleList.sort(key=lambda x: len(x))

    for i in range(len(tupleSet)):
        if i == 0:
            answer.append(tupleList[i][i])
        else:
            for j in tupleList[i]:
                if j not in tupleSet[i-1]:
                    answer.append(j)
                    break
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))