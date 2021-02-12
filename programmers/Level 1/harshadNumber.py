# Programmers 02/12 2021
# 하샤드 수

def solution(x):
    answer = True
    tmpX = x
    tmp = 0
    while True:
        if x < 10:
            tmp += x
            break

        tmp += (x % 10)
        x = int(x/10)

    print(tmp)
    if tmpX % tmp != 0:
        answer = False

    return answer

print(solution(510))