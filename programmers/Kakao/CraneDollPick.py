# Programmers 02/05 2021
# KaKao 크레인 인형뽑기 게임

def solution(board, moves):
    answer = 0
    basket = []
    # board 5 x 5  moves 8
    for i in range(0, len(moves)): # i : 0~7
        for j in range(0, len(board)): # j : 0~4
            if board[j][moves[i]-1] != 0:
                basket.append(board[j][moves[i]-1])
                board[j][moves[i]-1] = 0
                break

    print(basket)
    high = len(basket)
    for n in range(high+1):
        for k in range(0, len(basket)-1):
            if basket[k] == basket[k+1]:
                del basket[k+1]
                del basket[k]
                answer += 2
                break
    print(basket)
    return answer

bd = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
mv = [1,5,3,5,1,2,1,4]
print(solution(bd, mv))