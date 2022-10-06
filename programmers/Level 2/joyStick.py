# Programmers 10/07 2022
# 조이 스틱

def solution(name):
    
    moves = []    
    for n in list(name):
        moves.append(min(abs(ord(n)-65), abs(91-ord(n))))
    
    if len(moves) == 1:
        return sum(moves)
    
    if moves.count(0) == 0:
        return sum(moves) + len(moves) - 1

    if moves.count(0) == len(moves):
        return 0
    
    min_move = 1e9
    for i in range(1, len(moves)):
        right, left = 0, 0
        
        tmp = 0
        while tmp < i:
            if moves[tmp] != 0:
                right = tmp
            tmp += 1
        
        tmp = len(moves)-1
        while tmp >= i:
            if moves[tmp] != 0:
                left = tmp
            tmp -= 1
        left = len(moves) - left
        if left == len(moves):
            left = 0
        
        min_move = min(min_move, 2*right+left, 2*left+right)
        
    return sum(moves) + min_move