# Programmers 02/25 2022
# N으로 표현

def makeContinuityNum(N, idx):
    res = 0
    for _ in range(idx+1):
        res = res * 10 + N
    return res

def solution(N, number):
    answer = 0
    arr = [set()]
    arr[0].add(N)

    for i in range(1, 8):
        tmp = set()
        for j in range(i):
            for a in arr[j]:
                for b in arr[i-j-1]:
                    tmp.add(a + b)
                    tmp.add(a * b)
                    tmp.add(a - b)
                    if b != 0:
                        tmp.add(a // b)
                    tmp.add(makeContinuityNum(N, i))
        arr.append(tmp)

    for i in range(len(arr)):
        if number in arr[i]:
            return i+1
    return -1

print(solution(2, 22222222))