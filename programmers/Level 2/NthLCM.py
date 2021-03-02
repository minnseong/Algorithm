# Programmers 03/02 2021
# N개의 최소공배수

def solution(arr):
    arr.sort()
    maxNum = max(arr)
    answer = max(arr)

    arr.pop()

    # 2 6 8
    while True:
        cnt = 0
        for i in arr:
            if answer % i == 0:
                cnt += 1

        if cnt == len(arr):
            break
        else:
            answer += maxNum

    return answer

print(solution([2,6,8,14]))