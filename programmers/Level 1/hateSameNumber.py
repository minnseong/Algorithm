# Programmers 01/15 2021
# 같은 숫자는 싫어

def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            answer.append(arr[i+1])
    return answer

array = [1,1,3,3,0,1,1]
print(solution(array))