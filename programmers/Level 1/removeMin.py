# Programmers 02/11 2021
# 제일 작은 수 제거하기

def solution(arr):
    if len(arr) == 1:
        return -1

    min = arr[0]
    for i in range(1, len(arr)):
        if min > arr[i]:
            min = arr[i]

    arr.remove(min)

    return arr

print(solution([4,3,2,1]))