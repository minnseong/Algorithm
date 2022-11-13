# Programmers 11/13 2022
# 2022 카카오뱅크 인턴 코딩 테스트 Q2
# 성공

def solution(money, minratio, maxratio, ranksize, threshold, months):

    krws = []
    for ratio in range(minratio, maxratio):
        idx = ratio-minratio+1
        krws.append([threshold+(idx-1)*ranksize, threshold+(idx*ranksize)-1, ratio])

    for _ in range(months):
        onwer_money = money - (money%100)
        isOver = True
        if onwer_money < threshold:
            continue
        else:
            for krw in krws:
                if krw[0] <= onwer_money < krw[1]:
                    money = money - (onwer_money * (krw[2] / 100))
                    isOver = False
                    break
        if isOver:
            money = money - (onwer_money * (maxratio / 100))

    return int(money)
