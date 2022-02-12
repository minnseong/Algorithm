# Programmers 02/13 2022
# 피보나치 수

''' 시간 초과!
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
'''

def solution(n):
    # answer = fibonacci(n) % 1234567
    answer = [0, 1]
    for i in range(2, n+1):
        answer.append(answer[i-1] + answer[i-2])

    return answer[-1] % 1234567

print(solution(5))