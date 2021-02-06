# Programmers 02/06 2021
# Kakao 메뉴 리뉴얼
from itertools import combinations


def solution(orders, course):
    answer = []
    for n in course:
        order_list = []
        count = {}
        for o in orders:
            order_list += combinations(sorted(o), n)

        for element in order_list:
            if element not in count:
                count[element] = 0
            count[element] += 1

        print(count, end="\n")

        for c in count:
            if count[c] == max(count.values()) and count[c] != 1:
                answer.append(''.join(c))

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
# print(solution(["ABCDE","AB","CD","ADE","XYZ","XYZ","ACD"],[2,3,5]))
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
