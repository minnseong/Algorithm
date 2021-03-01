# Programmers 01/19 2021
# 최댓값과 최솟값

def solution(s):
    num_array = []

    array = list(s.split(" "))
    print(array)

    for x in array:
        num_array.append(int(x))

    max_value = max(num_array)
    min_value = min(num_array)

    answer = str(min_value) + " " + str(max_value)
    return answer

solution(solution("1 2 3 4"))
