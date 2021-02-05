# Programmers 02/05 2021
# 주식 가격

def solution(prices):
    answer = []

    for i in range(len(prices)):
        tmp = prices[i]
        cnt = 0
        for j in range(i+1, len(prices)):
            if tmp > prices[j]:
                answer.append(j-i)
                break

            if tmp <= prices[j]:
                cnt += 1
                continue

        if cnt == len(prices) - i - 1:
            answer.append(cnt)

    return answer

print(solution([1,2,3,2,3]))