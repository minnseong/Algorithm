# Programmers 11/19 2022
# 2022 웍스모바일 인턴 코딩 테스트 Q1

def solution(numbers):
    if len(numbers) == 2:
        return abs(numbers[0]-numbers[1])

    positive_nums = []
    negative_nums = []

    for num in numbers:
        if num >= 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)

    positive_nums.sort()
    negative_nums.sort(reverse=True)

    sum_a = 0
    sum_b = 0

    while positive_nums:
        num = positive_nums.pop()

        if sum_a >= sum_b:
            sum_b += num
        else:
            sum_a += num

    while negative_nums:
        num = negative_nums.pop()

        if sum_a >= sum_b:
            sum_a += num
        else:
            sum_b += num

    answer = abs(sum_a - sum_b)
    return answer
