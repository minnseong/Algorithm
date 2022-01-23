# Programmers 01/23 2022
# 위클리 챌린지 - 5주차 모음사전

from itertools import product

# A E I O U
def solution(word):
    answer = 0
    word_ = ['A', 'E', 'I', 'O', 'U']
    product_list = []

    for i in range(1, len(word_)+1):
        product_list.extend(list(product(word_, repeat=i)))
    
    product_list.sort()

    return product_list.index(tuple(word))+1

print(solution("I"))