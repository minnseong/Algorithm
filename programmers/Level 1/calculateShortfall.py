# Programmers 08/24 2021
# 위클리 챌린지 - 1주차 부족한 금액 계산하기

def solution(price, money, count):

    for i in range(1, count+1):
        money -= i * price

    if money >= 0:
        return 0
    else:
        return money * (-1)


print(solution(3, 20, 4))
