# Programmers 02/12 2021
# 최대공약수와 최소공배수

def solution(n, m):
    answer = []

    if n >= m:
        for i in range(m, 0, -1):
            if n % i == 0 and m % i == 0:
                answer.append(i)
                break

        answer.append(int(n*m / answer[0]))

    else:
        for i in range(n, 0, -1):
            if n % i == 0 and m % i == 0:
                answer.append(i)
                break

        answer.append(int(n * m / answer[0]))

    return answer

print(solution(15, 21))

