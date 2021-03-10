# Programmers 03/10 2021
# 소수 만들기
from itertools import combinations


def solution(nums):
    answer = 0

    numList = list(combinations(nums, 3))
    # print(numList)

    for i in numList:
        flag = False
        print(sum(i))
        for j in range(2, sum(i)):
            if sum(i) % j == 0:
                flag = True
        if flag is False:
            answer += 1

    return answer

print(solution([1,2,3,4]))