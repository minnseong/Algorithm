# Programmers 11/06 2022
# 롤케이크 자르기

from collections import defaultdict

def solution(topping):
    answer = 0
        
    cake_topping1 = defaultdict(int)
    
    for t in topping:
        cake_topping1[t] += 1
    
    topping1_cnt = len(cake_topping1)

    topping2_cnt = 0
    cake_topping2 = defaultdict(int)
    for t in topping:
        cake_topping2[t] += 1
        if cake_topping2[t] == 1:
            topping2_cnt += 1
            
        cake_topping1[t] -= 1
        if cake_topping1[t] == 0:
            topping1_cnt -= 1
            del cake_topping1[t]
        
        if topping1_cnt == topping2_cnt:
            answer += 1
    
    return answer