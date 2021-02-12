# Programmers 02/12 2021
# 행렬의 덧셈

def solution(arr1, arr2):
    answer = []

    for i, j in zip(arr1, arr2):
        tmp = []
        for w, z in zip(i, j):
            tmp.append(w+z)
        answer.append(tmp)

    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))