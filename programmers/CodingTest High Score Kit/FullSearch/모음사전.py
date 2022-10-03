from itertools import product

def solution(word):
    
    cases = []
    for i in range(1, 6):
        cases.extend(product(['A', 'E', 'I', 'O', 'U'], repeat=i))
    
    cases.sort()
    
    return cases.index(tuple(word))+1

