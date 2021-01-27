# Programmers 01/27 2021
# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    index = -1

    for i in seoul:
        index += 1
        if i == "Kim":
            break

    answer = '김서방은 ' + str(index) + '에 있다'
    return answer

print(solution(["Jane", "Kim"]))