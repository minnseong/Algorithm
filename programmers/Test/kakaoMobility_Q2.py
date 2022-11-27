# Programmers 11/27 2022
# 2022 카카오 모빌리티 코딩 테스트 Q2

from collections import defaultdict

def solution(id_list, k):

    coupon = defaultdict(int)

    for ids in id_list:
        for user in set(ids.split(" ")):
            if coupon[user] < k:
                coupon[user] += 1

    return sum(coupon.values())