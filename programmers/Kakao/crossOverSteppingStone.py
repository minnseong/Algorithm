# Programmers 04/27 2022
# 징검다리 건너기

def solution(stones, k):
    answer = []

    start = 1
    end = max(stones)+1

    while start <= end:
        
        mid = (start + end) // 2
        flag = False
        zeroCnt = 0
        for s in stones:
            if s - mid <= 0:
                zeroCnt += 1
                if zeroCnt == k:
                    answer.append(mid)
                    flag = True
                    break
            else:
                zeroCnt = 0

        if flag:
            end = mid - 1
        else:
            start = mid + 1

    return min(answer)

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))

'''
시간 초과 코드 ...!!

def solution(stones, k):
    answer = 0

    while True:
        zeroCnt = 0
        flag = False
        for i in range(len(stones)):
            if stones[i] == 0:
                zeroCnt +=1 
            else:
                stones[i] -= 1
                zeroCnt = 0
            
            if zeroCnt >= k:
                flag = True
                break
        if flag:
            break
        answer += 1

    return answer
'''

