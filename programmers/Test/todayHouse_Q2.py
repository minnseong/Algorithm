# 07/16 2022 - Q2
# 오늘의 집 - Software Engineer, Intern, Corp Engineering

def solution(target):
    answer = ''

    board = dict()

    x, y = 0, 0
    for i in range(26):
        board[chr(97+ i)] = [x, y]
        y += 1
        if y == 5:
            y = 0
            x += 1

    cursor = 'a'
    for t in target:
        moveX, moveY = board[t][0] - board[cursor][0], board[t][1] - board[cursor][1]

        if moveX > 0:
            answer += ('D' * moveX)
        elif moveX < 0:
            answer += ('U' * -moveX)

        if moveY > 0:
            answer += ('R' * moveY)
        elif moveX < 0:
            answer += ('L' * -moveY)

        answer += '!'
        cursor = t

    return answer

# [0, 1] -> [5, 0] : moveX = 5 moveY = -1