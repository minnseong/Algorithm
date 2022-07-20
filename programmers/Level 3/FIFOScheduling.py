# Programmers 07/20 2022
# 선입 선출 스케줄링

def solution(n, cores):
    answer = 0

    if n <= len(cores):
        return n
    
    start, end = 0, max(cores) * n
    mid = 0
    while start <= end:
        mid = (start + end) // 2

        tmp = 0
        for c in cores:
            tmp += (mid // c)

        if tmp >= n:
            end = mid - 1
        else:
            start = mid + 1
    
    for c in cores:
        n -= (start-1) // c

    for i in range(len(cores)):
        if start % cores[i] == 0:
            n -= 1
            if n == 0:
                return i+1

print(solution(9, [3,2,1,3]))

# (1, 1) (2, 2) (3, 3)

# 3 2 1 3
# 1번 : 1
# 2번 : 2
# 4번 : 3
# 5번 : 4
# 6번 : 3
# 7번 : 2
# 8번 : 3
# 9번 : 1

