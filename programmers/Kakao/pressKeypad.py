# Programmers 04/05 2021
# KaKao 키패드 누르기

def solution(numbers, hand):
    answer = ''
    left, right = "*", "#"
    pad = [["*", 0, "#"], [7, 8, 9], [4, 5, 6], [1, 2, 3]]

    for i in range(len(numbers)):
        if numbers[i] in [1, 4, 7]:
            answer += "L"
            left = numbers[i]
        elif numbers[i] in [3, 6, 9]:
            answer += "R"
            right = numbers[i]
        else:
            tmp = [0, 0, 0]
            for x in range(len(pad)):
                for y in range(len(pad[0])):
                    if pad[x][y] == numbers[i]:
                        tmp[0] = (x, y)
                    if pad[x][y] == left:
                        tmp[1] = (x, y)
                    if pad[x][y] == right:
                        tmp[2] = (x, y)

            if abs(tmp[0][0]-tmp[1][0]) + abs(tmp[0][1]-tmp[1][1]) > abs(tmp[0][0]-tmp[2][0]) + abs(tmp[0][1]-tmp[2][1]):
                answer += "R"
                right = numbers[i]
            elif abs(tmp[0][0]-tmp[1][0]) + abs(tmp[0][1]-tmp[1][1]) < abs(tmp[0][0]-tmp[2][0]) + abs(tmp[0][1]-tmp[2][1]):
                answer += "L"
                left = numbers[i]
            else:
                if hand == "right":
                    answer += "R"
                    right = numbers[i]
                else:
                    answer += "L"
                    left = numbers[i]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))