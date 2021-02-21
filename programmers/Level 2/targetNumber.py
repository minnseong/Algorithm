# Programmers 02/20 2021
# 타겟 넘버
# The Rest Of The Study
# DFS Algorithm

def solution(numbers, target):
    answer = 0
    stack = [[0, 0]]

    while stack:
        index, value = stack.pop()

        if index < len(numbers):
            stack.append([index+1, value-numbers[index]])
            stack.append([index+1, value+numbers[index]])
        else:
            if value == target:
                answer += 1

    return answer

print(solution([1,1,1,1,1], 3))

