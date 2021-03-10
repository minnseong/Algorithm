# Programmers 03/10 2021
# 폰켓몬

def solution(nums):
    answer = 0
    dic = {}

    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    if len(dic) < len(nums) // 2:
        answer = len(dic)
    else:
        answer = len(nums) // 2

    return answer

print(solution([3,3,3,2,2,4]))

