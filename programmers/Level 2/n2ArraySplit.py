# Programmers 12/10 2021
# n^2 배열 자르기

def solution(n, left, right):
    answer = []
    arr = [[0]*n for _ in range(n)]

    for i in range(n):
        tmp = 1+i
        for j in range(n):
            arr[i][j] = tmp
            if tmp <= j+1:
                tmp += 1
    
    # 시간초과로 2중 for문으로 2차원 배열을 1중 for문으로 2차원 배열을 만들려했지만 같음.
    # tmp = 1
    # for i in range(n*n):    
    #     arr[int(i/n)][i%n] = tmp
    #     if tmp <= i%n+1:
    #         tmp += 1
    #     if int((i+1)/n) != int(i/n):
    #         tmp = int((i+1)/n) + 1

    newArray = []
    for i in range(n):
        newArray.extend(arr[i])
    
    for i in range(left, right+1, 1):
        answer.append(newArray[i])

    return answer

print(solution(3, 2, 5))