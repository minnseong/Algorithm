# Programmers 02/24 2022
# 입국심사

def solution(n, times):

    start = 0
    end = max(times) * n

    while (start <= end):
        mid = (start + end) // 2
        
        total = 0
        for t in times:
            total += (mid // t)
        
        if (total >= n):
            end = mid - 1
        else:
            start = mid + 1

    return start

print(solution(6, [7, 10]))