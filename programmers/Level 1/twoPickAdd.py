# Programmers 01/29 2021
# 두 개 뽑아서 더하기

def solution(numbers):

    num = 0
    answer = []

    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)

    return sorted(answer)

print(solution([5,0,2,7]))