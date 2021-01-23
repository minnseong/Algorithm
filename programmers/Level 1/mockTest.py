# Programmers 01/23 2021
# 모의고사

def solution(answers):
    answer = []
    score = [0, 0, 0]
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(0, len(answers)):
        if answers[i] == student_1[i % len(student_1)]:
            score[0] += 1
        if answers[i] == student_2[i % len(student_2)]:
            score[1] += 1
        if answers[i] == student_3[i % len(student_3)]:
            score[2] += 1

    winner = max(score[0], score[1], score[2])

    if winner == score[0]:
        answer.append(1)
    if winner == score[1]:
        answer.append(2)
    if winner == score[2]:
        answer.append(3)

    return answer

print(solution([1,2,3,4,5]))