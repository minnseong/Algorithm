# 07/16 2022 - Q1
# 오늘의 집 - Software Engineer, Intern, Corp Engineering

def solution(arr):
    answer = 0

    subArraySum = list()

    for i in range(1, len(arr)):
        arr[i] = arr[i] + arr[i-1]

    for i in range(len(arr)):
        subArraySum.append(arr[i])
        for j in range(0, i):
            subArraySum.append(arr[i] - arr[j])

    for s in subArraySum:
        if s & 1:
            answer += 1

    return answer