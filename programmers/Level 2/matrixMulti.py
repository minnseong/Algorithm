# Programmers 03/03 2021
# 행렬의 곱셈

def solution(arr1, arr2):
    answer = []
    newArr2 = []

    for index in range(0, len(arr2[0])):
        tmp = []
        for i in arr2:
            tmp.append(i[index])
        newArr2.append(tmp)

    for i in arr1:
        arrTmp = []
        for j in newArr2:
            temp = 0
            for n in range(len(arr1[0])):
                temp += i[n]*j[n]
            arrTmp.append(temp)
        answer.append(arrTmp)

    return answer

print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]],[[5, 4, 3], [2, 4, 1], [3, 1, 1]]))
