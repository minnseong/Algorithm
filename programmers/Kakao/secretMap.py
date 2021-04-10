# Programmers 04/08 2021
# KaKao [1차] 비밀지도

def convertBinary(n):
    binary = format(n, 'b')
    return binary


def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = convertBinary(arr1[i])
        while len(tmp) != n:
            tmp = '0' + tmp
        arr1[i] = tmp

    for i in range(n):
        tmp = convertBinary(arr2[i])
        while len(tmp) != n:
            tmp = '0' + tmp
        arr2[i] = tmp

    for i in range(n):
        tmp = ""
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer

print(convertBinary(46))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))