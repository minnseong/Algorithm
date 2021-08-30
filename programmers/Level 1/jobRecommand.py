# Programmers 08/24 2021
# 위클리 챌린지 - 4주차 직업군 추천하기

def solution(table, languages, preference):
    jobDic = {1: "CONTENTS", 2: "GAME", 3: "HARDWARE", 4: "PORTAL", 5: "SI"}
    dic = {}
    order = [1, 4, 2, 3, 0]

    for t in range(len(table)):
        job = table[order[t]].split()
        dic[t+1] = {}
        for i in range(1, 6):
            dic[t+1][job[i]] = 6-i

    sum = []
    for i in range(1, 6):
        tmp = 0
        for j in range(len(languages)):
            try:
                tmp += dic[i][languages[j]] * preference[j]
            except:
                pass
        sum.append(tmp)

    maxIdx = sum.index(max(sum))
    answer = jobDic[maxIdx+1]

    return answer


print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
