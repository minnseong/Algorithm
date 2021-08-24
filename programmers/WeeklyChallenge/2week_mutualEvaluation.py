def avg(arr, idx):
    sumScore = sum(arr)
    idxScore = arr[idx]
    arr.remove(idxScore)

    maxScore = max(arr)
    minScore = min(arr)

    if idxScore > maxScore or idxScore < minScore:
        sumScore -= idxScore
        return sumScore / len(arr)
    else:
        return sumScore / (len(arr)+1)


def getGrade(avgScore):
    if avgScore >= 90:
        grade = "A"
    elif 80 <= avgScore < 90:
        grade = "B"
    elif 70 <= avgScore < 80:
        grade = "C"
    elif 50 <= avgScore < 70:
        grade = "D"
    else:
        grade = "F"

    return grade


def solution(scores):
    answer = ''

    myScore = []
    for i in range(len(scores)):
        tmp = []
        for s in scores:
            tmp.append(s[i])
        myScore.append(tmp)

    for s in range(len(myScore)):
        avgScore = avg(myScore[s], s)
        print(avgScore)
        answer += getGrade(avgScore)

    return answer


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
      47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))
