# Programmers 02/05 2021
# 기능 개발

def solution(progresses, speeds):
    answer = []
    dateList = []

    for p, s in zip(progresses, speeds):
        tmp = (100 - p) / s
        if tmp > int(tmp):
            tmp = int(tmp) + 1
        dateList.append(int(tmp))

    print(dateList)

    n = 0
    while True:
        tmp = dateList[n]
        if n == len(dateList) - 1:
            answer.append(1)

        for j in range(n+1, len(dateList)):
            if tmp < dateList[j]:
                answer.append(j-n)
                n = j
                break
            elif j == len(dateList)-1:
                answer.append(j-n+1)
                n = j
                break

        if sum(answer) == len(dateList):
            break

    return answer

#print(solution([93,30,55], [1,30,5]))
print(solution([95,90,99,99,80,99],[1,1,1,1,1,1]))