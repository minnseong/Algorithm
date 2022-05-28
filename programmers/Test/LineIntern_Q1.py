# Programmers 05/28 2022
# 2022 라인 인턴 코딩 테스트 Q1

def solution(logs):
    answer = []

    testDic = dict()
    userSet = set()
    for l in logs:
        user, test = l.split()
        userSet.add(user)
        if test in testDic:
            testDic[test].add(user)
        else:
            testDic[test] = set([user])

    userCnt = len(userSet)
    for k in testDic.keys():
        if len(testDic[k]) >= (userCnt / 2):
            answer.append(k)

    answer.sort()
    return answer

# print(solution(["morgan string_compare", "felix string_compare", "morgan reverse", "rohan sort", "andy reverse", "morgan sqrt"]))
# print(solution(["morgan sort", "felix sort", "morgan sqrt", "morgan sqrt", "rohan reverse", "rohan reverse"]))
# print(solution(["kate sqrt"]))

print(solution(["a aa","a bb", "a cc", "b cc", "c aa"]))