# Programmers 11/23 2022
# 할인 행사

from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    
    sale_items = defaultdict(int)
    
    for i in range(9):
        sale_items[discount[i]] += 1
    
    for i in range(9, len(discount)):
        sale_items[discount[i]] += 1
        if i >= 10:
            sale_items[discount[i-10]] -= 1
        
        cnt = 0
        for idx, item in enumerate(want):
            if sale_items[item] >= number[idx]:
                cnt += 1
            else:
                break

        if cnt == len(want):
            answer += 1
    return answer