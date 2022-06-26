# Programmers 06/26 2022
# 하노이 탑

def solution(n):
    answer = []

    def hanoi(n, src, dest, assi):
        if n == 1:
            answer.append([src, dest])
            return
        hanoi(n-1, src, assi, dest)
        answer.append([src, dest])
        hanoi(n-1, assi, dest, src)

    hanoi(n, 1, 3, 2)
    return answer

print(solution(2))

