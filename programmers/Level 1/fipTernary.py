# Programmers 01/21 2021
# 3진법 뒤집기

def solution(n):
    answer = 0
    tmp_str = ""

    while n != 0:
        tmp_str += str(n % 3)
        n = int(n / 3)

    # 1 - tmp = 45%3 = 0 , n = 15
    # 2 - tmp = 15%3 = 0 , n = 5
    # 3 - tmp = 5%3 = 2 , n = 1
    # 4 - tmp = 1%3 = 1 , n = 0
    # tmp = 0021

    jisu = 0
    for index in range(len(tmp_str)-1, -1, -1):
        answer += int(tmp_str[index]) * (3 ** jisu)
        jisu = jisu + 1

    return answer

print(solution(125))