# Programmers 02/01 2021
# 위장

def solution(clothes):
    answer = 1
    array = []
    num_array = []

    for i in range(len(clothes)):
        array.append(clothes[i][1])

    array.sort()

    cnt = 0
    for i in range(1, len(array)):
        if array[i-1] != array[i]:
            if not num_array:
                num_array.append(i)
            else:
                num_array.append(i - sum(num_array))
                cnt += 1

    num_array.append(len(array) - sum(num_array))

    print(array)
    print(num_array)

    for i in range(len(num_array)):
        answer *= (num_array[i]+1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))